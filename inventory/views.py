from django.shortcuts import render
from django.http import HttpResponse
from inventory.models import Producto

from django.core.paginator import Paginator

from inventory import utils

from django.views.decorators.csrf import csrf_exempt

import json
import urllib

from django.http import QueryDict


# Create your views here.

def searchproductscreen(request):
	return render(request,'searchproduct.html')

def returnproductpage(request,pagenumber=1,filter='none'):
	
	products=None

	if filter.isdigit():
		products = Producto.objects.filter(codigo=int(filter))
	elif filter != 'none':
		products = Producto.objects.filter(nombre__startswith=filter)
	else:
		products = Producto.objects.all();

	pages = Paginator(products,3)
	numberofpages= pages.num_pages
	currentpage=pages.page(pagenumber)
	listofpages=[x+1 for x in range(numberofpages)]
	return render(request,'productpage.html',{'numberofpages':listofpages, 'currentpage':currentpage})

def modifyproductscreen(request,productid):
	product=utils.getproductinformation(productid);
	stores=utils.getallstores();
	tp=utils.gettype(productid);
	return render(request,'modifyproduct.html',{'product':product,'stores':stores,'type':tp})

@csrf_exempt
def modifyproductaction(request):
	print(request.body)
	data=QueryDict(request.body)['mydata']
	print(data)
	#response=utils.saveproductchanges(urllib.unquote(request.body))
	response=utils.saveproductchanges(data)
	return HttpResponse(json.dumps({'funca':'funca'}))
