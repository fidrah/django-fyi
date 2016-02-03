import json

from inventory.models import Producto,Precios,Tienda,PreciosTienda,Inventario


def getproductinformation(data):
	
	datajson=json.loads(data)

	productoactual= Producto.objects.filter(codigo=datajson['codigo'])[0]

	tiendaactual= Tienda.objects.filter(nombre='Heredia Centro')[0]

	preciostienda= PreciosTienda.objects.filter(tienda=tiendaactual,precios__idproducto=productoactual)
	
	inventario= Inventario.objects.filter(producto=productoactual, tienda=tiendaactual)[0]
	print(inventario)

	data={}

	data.update({'producto':{'id':productoactual.id,'codigo':productoactual.codigo,'nombre':productoactual.nombre,'tipo':productoactual.tipo.nombre}})

	lsprecios=[{'cantidad':int(ps.precios.cantidad),'precio':int(ps.precios.precio)} for ps in preciostienda]

	data.update({'precios':lsprecios})

	data.update({'inventario':inventario.cantidad})

	print("listo")
	return json.dumps(data)