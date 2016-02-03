from django.contrib import admin
from inventory.models import Tipo, Producto, Precios, PreciosTienda, Tienda, Inventario
# Register your models here.

admin.site.register(Tipo)
admin.site.register(Producto)
admin.site.register(Precios)
admin.site.register(PreciosTienda)
admin.site.register(Tienda)
admin.site.register(Inventario)