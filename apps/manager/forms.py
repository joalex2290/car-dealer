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
        widgets = {
            'nombre': forms.TextInput(attrs={'required': 'true'}),
            'apellido': forms.TextInput(attrs={'required': 'true'}),
            'email': forms.TextInput(attrs={'required': 'true'}),
            'telefono': forms.TextInput(attrs={'required': 'True'}),
        }

    ROLES= (('Gerente', 'Gerente'),('Vendedor','Vendedor'),('Jefe Taller','Jefe Taller'))
    rol = forms.ChoiceField(choices=ROLES, required=True, label='Rol')
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all() , empty_label=None)    

class SucursalForm(forms.ModelForm):

    class Meta:
        model = Sucursal
        fields = ['nombre','telefono','direccion','ciudad',]
        labels = {'nombre':'Nombre', 
                  'telefono': 'Teléfono',
                  'direccion': 'Dirección',
                  'ciudad': 'Ciudad',}
        widgets = {
        'nombre': forms.TextInput(attrs={'required': 'true'}),
        'telefono': forms.TextInput(attrs={'required': 'true'}),
        'direccion': forms.TextInput(attrs={'required': 'true'}),
        'ciudad': forms.TextInput(attrs={'required': 'true'}),}

class FabricanteForm(forms.ModelForm):

    class Meta:
        model = Fabricante
        fields = ['nombre',]
        labels = {'nombre':'Nombre', }
        widgets = {
        'nombre': forms.TextInput(attrs={'required': 'true'}),}