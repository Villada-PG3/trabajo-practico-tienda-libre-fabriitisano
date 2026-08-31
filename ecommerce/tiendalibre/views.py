from django.shortcuts import render

def home(request):
    productos_destacados = [
        {"nombre": "Auriculares", "precio": 15000, "stock" : 5 },
        {"nombre": "Teclado", "precio": 11000, "stock" : 0 },
        {"nombre": "Mouse", "precio": 5000, "stock" : 12},
        {"nombre": "Camara", "precio": 10000, "stock": 4},
        {"nombre": "Pendrive ", "precio": 6000, "stock": 6},
        {"nombre": "USB", "precio": None, "stock": 0},

    ]
    context = {
        "titulo" : "ofertas de la semana",
        "productos": productos_destacados,
        "usuario_logueado": True
    }
    return render(request, 'tiendalibre/home.html', context)

def acerca_de(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')
