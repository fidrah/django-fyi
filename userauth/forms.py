from django import forms

class Logindata(forms.Form):
	usuario= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
	clave= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Clave'}))
	