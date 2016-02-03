from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import Logindata

def loginscreen(request):
	form = Logindata()
	c={}
	c.update(csrf(request))
	return render(request, 'login.html', {'form':form})

def authenticatelogin(request):
	# get user credentials an validate them using the authenticate method
	form= Logindata(request.POST)
	if form.is_valid():
		username=form.cleaned_data['usuario']
		userpassword=form.cleaned_data['clave']
		user = authenticate(username=username, password=userpassword)
		print(user.username)

#@login_required
#def testmethod(request):
#	print('hello')
#	return True