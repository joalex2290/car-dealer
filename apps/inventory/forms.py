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

    MODELO = (('0000', 'No Aplica'),('2000', '2000'),('2001','2001'),('2002', '2002'),('2003','2003'),('2004', '2004'),('2005','2005'),
              ('2006', '2006'),('2007','2007'),('2008', '2008'),('2009','2009'),('2010', '2010'),('2011','2011'),
              ('2012', '2012'),('2013','2013'),('2014', '2014'),('2015','2015'),('2016', '2016'))

    codigo = forms.CharField(widget=forms.TextInput(attrs={'required':'true'}))
    fabricante = forms.ModelChoiceField(queryset=Fabricante.objects.all() , empty_label=None)
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'required':'true'}))
    modelo = forms.ChoiceField(choices=MODELO, required=True)
    costo = forms.IntegerField(widget=forms.NumberInput(attrs={'required':'true'}))