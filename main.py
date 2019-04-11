import markdown
from bottle import route, run, view, abort
import io
from os import path
from collections import deque

siteDir = path.abspath("site")

pathCache = {}

@route('/')
def index():
    return getFile("/")


@route('/<doc:path>')
@view('page')
def getFile(doc):
    inputPath = path.normpath(path.join(siteDir, doc.strip("/\\")))

    if inputPath in pathCache:
        return pathCache[inputPath]

    pathBits = deque()
    sourceFile = None
    addIndex = False
    itemPath = inputPath

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
    page["offset"] = ".".join(pathBits)
    print(page["offset"])

    if addIndex:
        sourceFile = path.join(sourceFile, "index")
    
    with io.BytesIO() as output, open(sourceFile + ".md", "rb") as code:
        markdown.markdownFromFile(input=code, output=output)
        page["contents"] = output.getvalue()
        pathCache[inputPath] = page
        return page


run(host='localhost', port=8080, reloader=True)
