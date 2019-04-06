import markdown
from bottle import route, run, view, abort
import io
from os import path
from collections import deque

siteDir = path.abspath("site")

@route('/')
def index():
    return getFile("/")


@route('/<doc:path>')
@view('page')
def getFile(doc):
    itemPath = path.normpath(path.join(siteDir, doc.strip("/\\")))
    pathBits = deque()
    sourceFile = None
    addIndex = False

    while sourceFile is None:
        if path.isfile(itemPath + ".md"):
            sourceFile = itemPath
            break
        if path.isdir(itemPath) and path.isfile(path.join(itemPath,"index.md")):
            sourceFile = sourceFile = itemPath
            addIndex = True
            break
        if not itemPath.startswith(siteDir):
            abort(404, "Invalid article")
        itemPath, pathBit = path.split(itemPath)
        pathBits.appendleft(pathBit)
        print(itemPath, pathBits)

    pagePath = path.relpath(sourceFile, siteDir)
    page={}
    page["path"] = pagePath

    if addIndex:
        sourceFile = path.join(sourceFile, "index")
    
    with io.BytesIO() as output, open(sourceFile + ".md", "rb") as code:
        markdown.markdownFromFile(input=code, output=output)
        page["contents"] = output.getvalue()
        return page


run(host='localhost', port=8080, reloader=True)
