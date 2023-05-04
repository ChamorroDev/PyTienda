from django.urls import path

from .views import registro , logear ,productosAdmin

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', registro, name="Registro"),
    path('login/', logear, name="Login"),
    path('productos/', productosAdmin, name="productosAdmin"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 