from django.contrib import admin
from django.urls import path, include
from .site import site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oficina.urls')),
]

admin.site.site_title = "Oficina site admin (DEV)"
admin.site.site_header = "Painel Administrativo Oficina"
admin.site.index_title = "Painel de Administração"