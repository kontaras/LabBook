import app
import bottle
import tempfile
import httpx
import uuid
import os


def run_page(pages, path):
    views_bak = bottle.TEMPLATE_PATH
    site_dir_bak = app.SITE_DIR
    try:
        with tempfile.TemporaryDirectory() as views_dir:
            bottle.TEMPLATE_PATH = [views_dir]
            path_delimiter = str(uuid.uuid4())
            offset_delimiter = str(uuid.uuid4())
            breadcrumb_delimiter = str(uuid.uuid4())
            subpages_delimiter = str(uuid.uuid4())
            contents_delimiter = str(uuid.uuid4())
            toc_delimiter = str(uuid.uuid4())
            with open(os.path.join(views_dir, "page.tpl"), "w") as view:
                view.write(path_delimiter)
                view.write(offset_delimiter)
                view.write(breadcrumb_delimiter)
                view.write(subpages_delimiter)
                view.write(contents_delimiter)
                view.write(toc_delimiter)
            client = httpx.Client(app=app.APP)
            resp = client.get(path)
            print(resp.text)
        pass
    finally:
        bottle.TEMPLATE_PATH = views_bak
        app.siteDir = site_dir_bak
