# *- coding: utf-8 -*
from django import forms

class LoginForm(forms.Form):
	usuario = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ingrese Usuario"}),)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Ingrese Contrasena"}),)