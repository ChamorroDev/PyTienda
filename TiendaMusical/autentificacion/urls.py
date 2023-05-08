from django.urls import path


from .views import registro , eliminarUsuario,logear ,productosAdmin,Crearproducto,eliminarProducto,CrearDisco,ListaUsuarios

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', registro, name="Registro"),
    path('login/', logear, name="Login"),
    path('productos/', productosAdmin, name="productosAdmin"),
    path('Crearproducto/', Crearproducto, name="Crearproducto"),
    path('eliminarProducto/<str:disco_id>/', eliminarProducto, name="eliminarProducto"),
    path('crearDisco/', CrearDisco, name="CrearDisco"),
    path('ListaUsuarios/', ListaUsuarios, name="ListaUsuarios"),
    path('eliminarUsuario/<str:disco_id>/', eliminarUsuario, name="eliminarUsuario"),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 