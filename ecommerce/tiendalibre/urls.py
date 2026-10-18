from django.urls import path
from .views import HomeView,TemplateView,CatalogoView,AcercaView,detalle_producto

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('acerca-de-mi/', AcercaView.as_view, name='acerca_de'),
    path('catalogo/', CatalogoView.as_view, name='catalogo'),
    path('producto/<int:pk>/', detalle_producto, name='detalle_producto'),
]
