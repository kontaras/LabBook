import markdown
from bottle import route, run, view, abort
import io
from os import path

siteDir = path.abspath("site")

@route('/')
def index():
    return getFile("/")


@route('/<doc:path>')
@view('page')
def getFile(doc):
    itemPath = path.normpath(path.join(siteDir, doc.strip("/\\")))
    pathBits = []
    
    while not path.isfile(itemPath + ".md"):
        if not itemPath.startswith(siteDir):
            abort(404, "Invalid article")
        itemPath, pathBit = path.split(itemPath)
        pathBits.append(pathBit)
        print(itemPath, pathBits)
    
    page={}
    page["path"] = doc
    
    with io.BytesIO() as output, open(itemPath + ".md", "rb") as code:
        markdown.markdownFromFile(input=code, output=output)
        page["contents"] = output.getvalue()
        return page


run(host='localhost', port=8080, reloader=True)
