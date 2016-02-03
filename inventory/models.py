from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tipo(models.Model):
	nombre= models.CharField(max_length=200);
	unidad= models.CharField(max_length=200);

	class Meta:
		verbose_name = "Unidades de producto"

	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.unidad)

class Producto(models.Model):
	nombre= models.CharField(max_length=200)
	codigo= models.CharField(max_length=200)
	tipo= models.ForeignKey(Tipo)
	fecharegistro= models.DateTimeField(auto_now_add=True)
	usuarioregistro= models.ForeignKey(User)

	class Meta:
		verbose_name = "Producto"

	def __unicode__(self):
		return u'%s' % (self.nombre)

class Precios(models.Model):
	idproducto=models.ForeignKey(Producto)
	cantidad= models.IntegerField()
	precio= models.DecimalField(decimal_places=2, max_digits=9)

	class Meta:
		verbose_name = "Precio"

	def __unicode__(self):
		return u'%s / Cantidad: %s %s / Precio: %s' % (self.idproducto, self.cantidad, self.idproducto.tipo.nombre, self.precio)

class Tienda(models.Model):
	nombre= models.CharField(max_length=200)
	cedulaJuridica= models.CharField(max_length=200)

	class Meta:
		verbose_name = "Tienda"

	def __unicode__(self):
		return u'%s' % (self.nombre)

class PreciosTienda(models.Model):
	precios= models.ForeignKey(Precios)
	tienda= models.ForeignKey(Tienda)

	class Meta:
		verbose_name = "Precio en tienda"

	def __unicode__(self):
		return u'Tienda: %s / Producto: %s / Cantidad: %s / Precio: %s' % (self.tienda, self.precios.idproducto.nombre, self.precios.cantidad, self.precios.precio)

class Inventario(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = cantidad= models.IntegerField()
	tienda = models.ForeignKey(Tienda)

	class Meta:
		verbose_name = "Inventario"

	def __unicode__(self):
		return u'Tienda: %s / Producto: %s / Cantidad: %s %s' % (self.tienda.nombre, self.producto.nombre, self.cantidad, self.producto.tipo.nombre)



