from django.shortcuts import render, get_object_or_404
from .models import Producto

def home(request):
    
    productos_destacados = Producto.objects.order_by("-id")[:3]


    context = {
        "titulo" : "Recien Agregados",
        "productos": productos_destacados,
        "usuario_logueado": True
    }
    return render(request, 'tiendalibre/home.html', context)

def acerca_de(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')

def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by("-nombre")
    context = {
        "productos":productos
    }
    return render(request,"tiendalibre/catalogo.html",context)

def detalle_producto(request,pk):
    producto = get_object_or_404(Producto,pk=pk)
    return render (request,"tiendalibre/detalle.html",{"producto":producto})

