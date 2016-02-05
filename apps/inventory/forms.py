# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from models import Articulo
from apps.manager.models import Fabricante

class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['codigo','tipo','fabricante','descripcion','modelo','costo']
        labels = {'codigo':'Código', 
                  'tipo': 'Tipo',
                  'fabricante':'Fabricante',
                  'descripcion': 'Descripción', 
                  'modelo':'Modelo',
                  'costo':'Costo',}