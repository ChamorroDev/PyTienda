from django.urls import path

from .views import tienda , formato

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', tienda, name="Tienda"),
    path('formato/<int:formato_id>/',formato, name="formato"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 