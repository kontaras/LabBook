"""
The main application file
"""

import io
import os
from collections import deque
from os import path

import markdown
from bottle import view, abort, Bottle

SITE_DIR = path.abspath("site")

PATH_CACHE = {}

APP = Bottle()

MD = markdown.Markdown(extensions=['toc'])


@APP.route('/')
def index():
    """
    Default route for the root of the server
    :return: The top level page
    """
    return get_file("/")


@APP.route('/<doc:path>')
@view('page')
def get_file(doc):
    """
    Generate a page for a given article
    :param doc: The article path
    :return: The template substitutions for the article
    """
    input_path = path.normpath(path.join(SITE_DIR, doc.strip("/\\")))

    if input_path in PATH_CACHE:
        return PATH_CACHE[input_path]

    path_bits = deque()
    content = None
    item_path = input_path

    while content is None:
        if path.isfile(item_path + ".md"):
            content = get_markdown_content(item_path + ".md")
            toc = MD.toc
            break
        if path.isdir(item_path):
            if path.isfile(path.join(item_path, "index.md")):
                content = get_markdown_content(path.join(item_path,
                                                         "index.md"))
                toc = MD.toc
            else:
                content = ""
                toc = ""
            break
        if not item_path.startswith(SITE_DIR):
            abort(404, "Invalid article")
        item_path, path_bit = path.split(item_path)
        path_bits.appendleft(path_bit)
        print(item_path, path_bits)

    page_path = path.relpath(item_path, SITE_DIR)
    page = {}
    page["path"] = page_path
    page["offset"] = ".".join(path_bits)
    print(page["offset"])
    page["breadcrumb"] = "/".join(
        map(lambda x: "<a href='%s'>%s</a>" % (x[1], x[0]),
            generate_breadcrumb(page_path)))

    subpages = get_sub_pages(item_path)
    if len(subpages) > 0:
        buffer = "<ul>\n"
        for subpage in subpages:
            buffer += "<li><a href='/%s'>%s</a></li>\n" % \
                (path.join(page_path, subpage), subpage)
        buffer += "</ul>\n"
        page["subpages"] = buffer
    else:
        page["subpages"] = ""

    page["contents"] = content
    page["toc"] = toc
    PATH_CACHE[input_path] = page
    return page


def get_sub_pages(item_path):
    """
    Get a list of sub-pages of a give path
    :param item_path: The path relative to which to look for sub-pages
    :return: a list of sub-pages
    """
    if not path.isdir(item_path):
        return []
    subs = []
    for item in os.listdir(item_path):
        if item != "index.md":
            if path.isdir(path.join(item_path, item)):
                subs.append(item)
            else:
                root, ext = path.splitext(item)
                if ext == ".md":
                    subs.append(root)
    subs.sort()
    return subs


def generate_breadcrumb(page_path):
    """
    Build the bread crumb leading from a file path back to the root
    :param page_path: The relative file path
    :return: Tupples of the form (dirname, dirpath)
    """
    buffer = []
    pathbuf = ""
    for part in path.dirname(page_path).split("/"):
        if len(part) > 0:
            pathbuf += "/" + part
            buffer.append((part, pathbuf))
    buffer = [("Home", "/")] + buffer
    return buffer


def get_markdown_content(page_path):
    """
    Convert a markdown file to HTML
    :param page_path: The path to the file
    :return: The string HTML representation of the file
    """
    with io.BytesIO() as output, open(page_path, "rb") as code:
        MD.reset().convertFile(input=code, output=output)
        return output.getvalue()


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
