from django.views.generic import TemplateView,ListView
from .models import Producto



class HomeView(TemplateView):
    template_name= "tiendalibre/home.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["productos"] = Producto.objects.all()
        return context
    
class CatalogoView(ListView):
    model= Producto
    template_name="tiendalibre/catalogo.html"
    context_object_name = "productos"

class AcercaView(TemplateView):
    template_name= "tiendalibre/acerca.html"    

