from django.urls import path

from inicio import views

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="Home"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)