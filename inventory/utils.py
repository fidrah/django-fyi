from inventory.models import Producto,Precios,Tienda,PreciosTienda,Inventario
import json

from decimal import *

def getproductinformation(productid):

	data={}

	product=Producto.objects.filter(id=productid)[0];
	data.update({'product':{'id':product.id,'nombre':product.nombre,'codigo':product.codigo}})

	precios=Precios.objects.filter(idproducto=productid)
	lsprecios=[]

	for precio in precios:

		lsprecios.append({'action':'modify','id':precio.id,'cantidad':int(precio.cantidad),'precio':int(precio.precio),'tipo':product.tipo.nombre,'tiendas':insertstores(precio)})

	data.update({'precios':lsprecios})

	inventario=Inventario.objects.filter(producto=productid).order_by('tienda__nombre')

	data.update({'inventario':insertinventory(inventario,product)})

	return json.dumps(data)

def insertinventory(objs,product):
	lsinventario=[]
	currentstores=[]
	for inventarioentienda in objs:

		lsinventario.append({'nombretienda':inventarioentienda.tienda.nombre,'action':'modify','id':inventarioentienda.id,'cantidad':int(inventarioentienda.cantidad),'tipo':product.tipo.nombre,'mas':0,'menos':0})
		currentstores.append(inventarioentienda.tienda.nombre)

	tiendas=Tienda.objects.all()
	nombrestiendas=[y.nombre for y in tiendas]

	uncheckedstores=list(set(nombrestiendas)-set(currentstores))
	
	for unstore in uncheckedstores:
		lsinventario.append({'nombretienda':unstore,'action':'missing','cantidad':0,'mas':0,'menos':0,'tipo':product.tipo.nombre})

	return lsinventario

def insertstores(obj):
	storeprice=PreciosTienda.objects.filter(precios=obj.id)
	data=[]
	checkedstoresnames=[]

	for x in storeprice:
		checkedstoresnames.append(x.tienda.nombre)
		print(x.tienda.nombre)
		data.append({'nombre':x.tienda.nombre,'id':x.tienda.id,'Checked':True})

	tiendas=Tienda.objects.all()
	nombrestiendas=[y.nombre for y in tiendas]

	uncheckedstores=list(set(nombrestiendas)-set(checkedstoresnames))

	missingstores=Tienda.objects.filter(nombre__in=uncheckedstores)

	for x in missingstores:
		data.append({'nombre':x.nombre,'id':x.id,'Checked':False})

	return sorted(data)

def getallstores():
	stores=Tienda.objects.all();
	data=[]
	for store in stores:
		data.append({'Checked':False,'nombre':store.nombre,'id':store.id})

	return json.dumps(sorted(data))

def gettype(productid):
	tipo=Producto.objects.filter(id=productid)[0].tipo.nombre
	data={'value':tipo}
	return json.dumps(data)

def saveproductchanges(jsonobj):
	try:
		productjson=json.loads(jsonobj)
		product=Producto.objects.filter(id=productjson['product']['id'])[0]
		product.nombre=productjson['product']['nombre']
		product.codigo=productjson['product']['codigo']
		product.save()

		for tiendainventario in productjson['inventario']:
			if tiendainventario['action']=='modify':
				objinventario=Inventario.objects.filter(id=tiendainventario['id'])[0]
				cantidadactual=objinventario.cantidad

				if(int(tiendainventario['mas'])>0):
					cantidadactual+=int(tiendainventario['mas'])
				elif(int(tiendainventario['menos'])>0):
					cantidadactual-=int(tiendainventario['menos'])

				objinventario.cantidad=cantidadactual
				objinventario.save()
			elif tiendainventario['action']=='missing':
				tienda=Tienda.objects.filter(nombre=tiendainventario['nombretienda'])[0]
				objinventario= Inventario.objects.create(producto=product,cantidad=int(tiendainventario['mas']),tienda=tienda)

		for precio in productjson['precios']:
			if precio['action']== 'modify':

				objprecio=Precios.objects.filter(id=precio['id'])[0]
				objprecio.cantidad=precio['cantidad']
				objprecio.precio=precio['precio']
				objprecio.save()

				for tienda in precio['tiendas']:
					objtienda=Tienda.objects.filter(id=tienda['id'])[0]
					preciotienda=PreciosTienda.objects.filter(precios__id=precio['id'],tienda__id=tienda['id'])
					if tienda['Checked'] and len(preciotienda)==0:
						newpreciotienda=PreciosTienda.objects.create(precios=objprecio,tienda=objtienda)
					elif not tienda['Checked'] and len(preciotienda)>0:
						preciotienda[0].delete()

			elif precio['action']== 'new':
				
				objprecio=Precios.objects.create(idproducto=product,cantidad=precio['cantidad'],precio=precio['precio'])
				for tienda in precio['tiendas']:
					if tienda['Checked']:
						objtienda=Tienda.objects.filter(id=tienda['id'])[0]
						newpreciotienda=PreciosTienda.objects.create(precios=objprecio,tienda=objtienda)

			elif precio['action']== 'delete':

				objprecio=Precios.objects.filter(id=precio['id'])[0]

				for tienda in precio['tiendas']:
					if tienda['Checked']:
						PreciosTienda.objects.filter(precios__id=precio['id'],tienda__id=tienda['id'])[0].delete()

				objprecio.delete()


	except Exception as e:
		return "error"
	else:
		return "Los cambios se realizaron correctamente"	























