import markdown
from bottle import route, run, view, abort
import io
from os import path
from collections import deque
import os

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
            sourceFile = itemPath
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
    page["breadcrumb"] = "/".join(generate_breadcrumb(pagePath))

    subpages = get_sub_pages(itemPath)
    if len(subpages) > 0:
        buffer = "<ul>\n"
        for subpage in subpages:
            buffer += "<li><a href='/%s'>%s</a></li>\n" % (path.join(pagePath, subpage), subpage)
        buffer += "</ul>\n"
        page["subpages"] = buffer
    else:
        page["subpages"] = ""

    if addIndex:
        sourceFile = path.join(sourceFile, "index")
    
    with io.BytesIO() as output, open(sourceFile + ".md", "rb") as code:
        markdown.markdownFromFile(input=code, output=output)
        page["contents"] = output.getvalue()
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
    for part in path.dirname("./" + pagePath).split("/"):
        buffer.append("<a href='/%s'>%s</a>" % (part, part))
    return buffer


run(host='localhost', port=8080, reloader=True)
