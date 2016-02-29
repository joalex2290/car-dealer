# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from models import Reparacion, ReparacionLinea
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from apps.manager.models import Sucursal
from apps.inventory.models import Articulo
from apps.sales.models import Cliente

class ReparacionForm(forms.ModelForm):
	class Meta:
		model = Reparacion

	id_reparacion = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'span1'}))
	total = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control pull-right','style':'margin-top:6px; margin-right:6px;','value':'0','readonly':'true'}))
	comentario = forms.CharField(widget=forms.Textarea(attrs={'rows':'2'}))

class ReparacionLineaForm(forms.ModelForm):
	class Meta:
		model = ReparacionLinea

	id_reparacion = forms.IntegerField(widget=forms.HiddenInput())
	articulo = forms.ModelChoiceField(widget=forms.Select,queryset=Articulo.objects.all().filter(is_active=True,tipo=2),initial=None)
	total_linea = forms.IntegerField(widget=forms.NumberInput(attrs={'value':'0','readonly':'true'}))

ReparacionLineaFormset = inlineformset_factory(Reparacion, ReparacionLinea, form=ReparacionLineaForm, extra=1)