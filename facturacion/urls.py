from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^facturar/vista', 'facturacion.views.facturacionview'),
    url(r'^facturar/buscarproducto', 'facturacion.views.obtenerinformaciondelproducto'),
]
