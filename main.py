import markdown
from bottle import route, run, HTTPError
import io
from os import path


@route('/')
def index():
    return getFile("README.md")


@route('/<doc:path>')
def getFile(doc):
    siteDir = path.abspath("site")
    fl = path.normpath(path.join(siteDir, doc + ".md"))
    if not fl.startswith(siteDir) or not path.exists(fl):
        raise HTTPError(status=404)
    with io.BytesIO() as output, open(fl, "rb") as code:
        markdown.markdownFromFile(input=code, output=output)
        return output.getvalue()


run(host='localhost', port=8080)
