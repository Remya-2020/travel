from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

from . models import Team


def demo(request):

    obj1=Team.objects.all()

    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
    #name="india"
    #return HttpResponse("Hello world")
    #return render(request,"index123.html",{'obj':name})
"""def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,"resultadd.html",{'result':res})


def about(request):
    return render(request,"aboiut.html")
def contact(request):
    return HttpResponse("contact")"""