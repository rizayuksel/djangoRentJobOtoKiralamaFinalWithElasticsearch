from django.shortcuts import render
from Search.documents import AutosDocument

# Create your views here.

def search(request):
    keyword = request.GET.get("keyword")
    if keyword:
        autos = AutosDocument.search().query("match", title=keyword)
    return render(request, "search.html", {"autos": autos})
