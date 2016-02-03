from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.http import QueryDict

import facturacion.utils
# Create your views here.

def facturacionview(request):
	return render(request,'facturacion.html')

@csrf_exempt
def obtenerinformaciondelproducto(request):
	print('entro')
	data=QueryDict(request.body)['mydata']
	information=utils.getproductinformation(data)
	print("paso")
	return HttpResponse(information)