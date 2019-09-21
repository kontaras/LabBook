import markdown
from bottle import view, abort, Bottle
import io
from os import path
from collections import deque
import os

siteDir = path.abspath("site")

pathCache = {}

app = Bottle()


@app.route('/')
def index():
    return getFile("/")


@app.route('/<doc:path>')
@view('page')
def getFile(doc):
    inputPath = path.normpath(path.join(siteDir, doc.strip("/\\")))

    if inputPath in pathCache:
        return pathCache[inputPath]

    pathBits = deque()
    content = None
    itemPath = inputPath

    while content is None:
        if path.isfile(itemPath + ".md"):
            content = get_markdown_content(itemPath + ".md")
            break
        if path.isdir(itemPath):
            if path.isfile(path.join(itemPath, "index.md")):
                content = get_markdown_content(path.join(itemPath, "index.md"))
            else:
                content = ""
            break
        if not itemPath.startswith(siteDir):
            abort(404, "Invalid article")
        itemPath, pathBit = path.split(itemPath)
        pathBits.appendleft(pathBit)
        print(itemPath, pathBits)

    pagePath = path.relpath(itemPath, siteDir)
    page = {}
    page["path"] = pagePath
    page["offset"] = ".".join(pathBits)
    print(page["offset"])
    page["breadcrumb"] = "/".join(
        map(lambda x: "<a href='%s'>%s</a>" % (x[1], x[0]),
            generate_breadcrumb(pagePath)))

    subpages = get_sub_pages(itemPath)
    if len(subpages) > 0:
        buffer = "<ul>\n"
        for subpage in subpages:
            buffer += "<li><a href='/%s'>%s</a></li>\n" % \
                (path.join(pagePath, subpage), subpage)
        buffer += "</ul>\n"
        page["subpages"] = buffer
    else:
        page["subpages"] = ""

    page["contents"] = content
    pathCache[inputPath] = page
    return page


def get_sub_pages(item_path):
    if not path.isdir(item_path):
        return []
    subs = []
    for item in os.listdir(item_path):
        if item != "index.md":
            if path.isdir(path.join(item_path, item)):
                subs.append(item)
            elif item.endswith(".md"):
                subs.append(item.rstrip(".md"))
    return subs


def generate_breadcrumb(pagePath):
    buffer = []
    pathbuf = ""
    for part in path.dirname(pagePath).split("/"):
        if len(part) > 0:
            pathbuf += "/" + part
            buffer.append((part, pathbuf))
    buffer = [("Home", "/")] + buffer
    return buffer


def get_markdown_content(pagePath):
    with io.BytesIO() as output, open(pagePath, "rb") as code:
        markdown.markdownFromFile(input=code, output=output)
        return output.getvalue()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
