from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Autos

# Create your views here.
def index(request):
    return render(request,"index.html")

def office(request):
    return render(request,"office.html")

def history(request):
    return render(request,"history.html")

def allCars(request):
    #keyword = request.GET.get("keyword")#arama yapmak için ESKİ ARAMA YAPISI
    #if keyword:
    #    allCars = Autos.objects.filter(title__contains = keyword)
    #    return render(request, "allcars.html", {"allCars":allCars})
    allCars = Autos.objects.all() #Autos veri tabanındaki tüm verileri sözlük yapısıyla aldık
    return render(request,"allcars.html",{"allCars":allCars})


def detail(request,id):
    auto =get_object_or_404(Autos, id = id)
    return render(request, "detail.html",{"auto":auto})

def audi(request):
    allCars = Autos.objects.filter(title__contains = "Audi")
    trademark = "Audi"
    return render(request,"trademark.html",{"allCars":allCars, "trademark" : trademark})

def bmw(request):
    allCars = Autos.objects.filter(title__contains = "Bmw")
    trademark = "Bmw"
    return render(request,"trademark.html",{"allCars":allCars, "trademark" : trademark})

def mazda(request):
    allCars = Autos.objects.filter(title__contains = "Mazda")
    trademark = "Mazda"
    return render(request,"trademark.html",{"allCars":allCars, "trademark" : trademark})

def volkswagen(request):
    allCars = Autos.objects.filter(title__contains = "Volkswagen")
    trademark = "Volkswagen"
    return render(request,"trademark.html",{"allCars":allCars, "trademark" : trademark})

def volvo(request):
    allCars = Autos.objects.filter(title__contains = "Volvo")
    trademark = "Volvo"
    return render(request,"trademark.html",{"allCars":allCars, "trademark" : trademark})

