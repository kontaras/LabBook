import markdown
from bottle import route, run, HTTPError, view
import io
from os import path


@route('/')
def index():
    return getFile("/")


@route('/<doc:path>')
@view('page')
def getFile(doc):
    siteDir = path.abspath("site")
    fl = path.normpath(path.join(siteDir, doc + ".md"))
    if not fl.startswith(siteDir) or not path.exists(fl):
        raise HTTPError(status=404)
    
    page={}
    page["path"] = doc
    
    with io.BytesIO() as output, open(fl, "rb") as code:
        markdown.markdownFromFile(input=code, output=output)
        page["contents"] = output.getvalue()
        return page


run(host='localhost', port=8080)
