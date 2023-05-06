from django.urls import path


from .views import registro , logear ,productosAdmin,Crearproducto

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('', registro, name="Registro"),
    path('login/', logear, name="Login"),
    path('productos/', productosAdmin, name="productosAdmin"),
    path('Crearproducto/', Crearproducto, name="Crearproducto"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 