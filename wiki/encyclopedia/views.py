from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if (util.get_entry(title)):
        content = util.get_entry(title)
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "content": content
        })
    return render(request, "encyclopedia/notfound.html")

