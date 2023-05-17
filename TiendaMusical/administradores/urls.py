from django.urls import path


from django.conf import settings

from django.conf.urls.static import static

from .views import *

listaLineaPedidos
urlpatterns = [
    path('productos/', productosAdmin, name="productosAdmin"),
    path('Crearproducto/', Crearproducto, name="Crearproducto"),
    path('eliminarProducto/<str:disco_id>/', eliminarProducto, name="eliminarProducto"),
    path('crearDisco/', CrearDisco, name="CrearDisco"),
    path('ListaUsuarios/', ListaUsuarios, name="ListaUsuarios"),
    path('eliminarUsuario/<str:disco_id>/', eliminarUsuario, name="eliminarUsuario"),
    path('editar_producto/<str:disco_id>/', editar_producto, name="editar_producto"),
    path('buscar-discos/', buscar_discos, name='buscar_discos'),
    path('editarUsuario/<str:userss>/', editarUsuario, name="editarUsuario"),
    path('listaPedidos/', listaPedidos, name="listaPedidos"),
    path('listaLineaPedidos/<str:linea_pedido>/', listaLineaPedidos, name="listaLineaPedidos"),

  

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 