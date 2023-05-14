from django.urls import path


from .views import registro , cerrar_sesion,logear 

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', registro, name="Registro"),
    path('login/', logear, name="Login"),
    path('logout', cerrar_sesion, name="cerrar_sesion"),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 