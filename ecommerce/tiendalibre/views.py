from django.shortcuts import render

def home(request):
    return render(request, 'tiendalibre/home.html')

def acerca_de(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')