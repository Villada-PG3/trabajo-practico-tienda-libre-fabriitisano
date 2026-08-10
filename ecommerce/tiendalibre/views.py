from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Bienvenidos a Tienda libre</h1>")

def acerca_de(request):
    return render(request,"tiendalibre/acerca-de-mi.html")