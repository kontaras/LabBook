"""
Utilities for common functionality for writing integration tests.
"""
import locale
import tempfile
import uuid
import os

import httpx
import bottle

import app


def run_page(pages, path):
    """
    Run the server with given pages and get the HTML generated from each page
    part.

    :param pages: The pages that the server should serve, as pairs of path and
    contents.
    :param path: Path from the server to load.
    :return: The page parts, in a dictionary.
    """
    views_bak = bottle.TEMPLATE_PATH
    site_dir_bak = app.SITE_DIR
    try:
        with tempfile.TemporaryDirectory() as views_dir, \
                tempfile.TemporaryDirectory() as site_dir:
            bottle.TEMPLATE_PATH = [views_dir]
            app.SITE_DIR = site_dir
            add_pages_to_site(site_dir, pages)

            path_delimiter = str(uuid.uuid4())
            offset_delimiter = str(uuid.uuid4())
            breadcrumb_delimiter = str(uuid.uuid4())
            subpages_delimiter = str(uuid.uuid4())
            contents_delimiter = str(uuid.uuid4())
            toc_delimiter = str(uuid.uuid4())
            with open(os.path.join(views_dir, "page.tpl"), "w",
                      encoding=locale.getpreferredencoding()) as view:
                write_section_to_view(view, "path", path_delimiter)
                write_section_to_view(view, "offset", offset_delimiter)
                write_section_to_view(view, "breadcrumb", breadcrumb_delimiter)
                write_section_to_view(view, "subpages", subpages_delimiter)
                write_section_to_view(view, "contents", contents_delimiter)
                write_section_to_view(view, "toc", toc_delimiter)
            client = httpx.Client(app=app.APP)
            resp = client.get("http://host/" + path)

            page = resp.text
            parts_dict = {}

            page = get_part(page, path_delimiter, parts_dict, "path")
            page = get_part(page, offset_delimiter, parts_dict, "offset")
            page = get_part(page, breadcrumb_delimiter, parts_dict,
                            "breadcrumb")
            page = get_part(page, subpages_delimiter, parts_dict, "subpages")
            page = get_part(page, contents_delimiter, parts_dict, "contents")
            page = get_part(page, toc_delimiter, parts_dict, "toc")

            assert len(page.strip()) == 0

            print(parts_dict)
            return parts_dict
    finally:
        bottle.TEMPLATE_PATH = views_bak
        app.siteDir = site_dir_bak


def add_pages_to_site(site_dir, pages):
    """
    Create all of the pages in the site dir.
    :param site_dir: Directory into which to write the pages.
    :param pages: Pairs of path and contents to use to create pages.
    """
    for path, contents in pages.items():
        file_path = os.path.join(site_dir, path + ".md")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w",
                  encoding=locale.getpreferredencoding()) as page:
            page.write(contents)


def write_section_to_view(view, template_var, delimiter):
    """
    Add a template variable into a view.
    :param view: The view the variable should be written into.
    :param template_var: The variable to write.
    :param delimiter: Delimiter to mark the end of the variable section.
    """
    view.write(f"{{{{!{template_var}}}}}\n")
    view.write(delimiter + "\n")


def get_part(page, delimiter, part_dict, key):
    """
    Extract the page contents that precede a delimiter and add it to a
    dictionary.

    :param page: The page contents.
    :param delimiter: Delimiter to separate the page from the desired part from
    the rest of the page.
    :param part_dict: Dictionary into which the part should be written.
    :param key: The key in the dict that the part should be written to.
    :return: The page after the delimiter.
    """
    part, _, rest = page.partition(delimiter)
    part_dict[key] = part.strip()
    return rest
