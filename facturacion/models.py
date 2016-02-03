from django.db import models
from inventory.models import Tienda, Producto
from django.contrib.auth.models import User
# Create your models here.

class Factura(models.Model):
	tienda= models.ForeignKey(Tienda)
	cancelada= models.BooleanField(default=False)
	fechacrecacion= models.DateTimeField(auto_now_add=True)
	total= models.IntegerField()
	usuario= models.ForeignKey(User)
	detalle= models.CharField(max_length=200)

class Detalle(models.Model):
	precio= models.IntegerField()
	cantidad= models.IntegerField()
	producto= models.ForeignKey(Producto)
	cancelado= models.BooleanField(default=False)

class FacturaDetalle(models.Model):
	factura= models.ForeignKey(Factura)
	detalle= models.ForeignKey(Detalle)

class Reimpresion(models.Model):
	factura= models.ForeignKey(Factura)
	usuario= models.ForeignKey(User)

class SolicitudCancelacion(models.Model):
	factura= models.ForeignKey(Factura)
	usuario= models.ForeignKey(User, related_name='requester')
	detalle= models.CharField(max_length=200)
	aceptado= models.BooleanField(default=False)
	admin= models.ForeignKey(User, related_name='approver')