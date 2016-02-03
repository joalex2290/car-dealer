# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from models import Cliente, Venta, VentaLinea
from apps.manager.models import Sucursal
from apps.inventory.models import Articulo

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

class VentasForm(forms.ModelForm):
	class Meta:
		model = Venta

class VentasLineaForm(forms.ModelForm):
	class Meta:
		model = VentaLinea