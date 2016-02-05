# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from models import Perfil, Sucursal, Fabricante

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password',]
        labels = {'username': 'Nombre de Usuario',
                  'password': 'Contraseña',}
        widgets = {
            'username': forms.TextInput(attrs={'required': 'true'}),
            'password': forms.PasswordInput(),
        }

class UserPassForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['password',]
        labels = {'password': 'Contraseña',}
        widgets = {
            'password': forms.PasswordInput(),
        }

class PerfilForm(forms.ModelForm):


    class Meta:
        model = Perfil
        fields = ['nombre','apellido','email','telefono','rol','sucursal',]
        labels = {'nombre':'Nombre', 
                  'apellido': 'Apellido',
                  'email': 'Email',                
                  'telefono': 'Teléfono',
                  'rol': 'Rol',
                  'sucursal':'Sucursal',}   

class SucursalForm(forms.ModelForm):

    class Meta:
        model = Sucursal
        fields = ['nombre','telefono','direccion','ciudad',]
        labels = {'nombre':'Nombre', 
                  'telefono': 'Teléfono',
                  'direccion': 'Dirección',
                  'ciudad': 'Ciudad',}


class FabricanteForm(forms.ModelForm):

    class Meta:
        model = Fabricante
        fields = ['nombre',]
        labels = {'nombre':'Nombre',}