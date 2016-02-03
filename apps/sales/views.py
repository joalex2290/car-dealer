from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, View, ListView, CreateView
from django.contrib.auth.models import User
from models import Cliente, Venta, VentaLinea
from forms import ClienteForm, VentasForm, VentasLineaForm
from django.forms.formsets import formset_factory

# Create your views here.

class VentaCreateView(TemplateView):
    ventaform = VentasForm(prefix='venta')
    ventalineaform = VentasLineaForm(prefix='venta_linea')
    template_name = 'sales/venta/add.html'
    ventalineaformset = formset_factory(VentasLineaForm)

    def get_context_data(self, **kwargs):
        context = super(VentaCreateView, self).get_context_data(**kwargs)
        if 'ventaform' not in context:
            context['ventaform'] = self.ventaform
        if 'ventalineaform' not in context:
            context['ventalineaform'] = self.ventalineaform
        if 'ventalineaformset' not in context:
            context['ventalineaformset'] = self.ventalineaformset
        return context

    def post(self, request,*args,**kwargs):
        ventaform = ventaform(request.POST, prefix='user')
        ventalineaform = ventalineaform(request.POST, prefix='perfil')
        if ventaform.is_valid() and ventalineaform.is_valid():

            venta = ventaform.save(commit=False)

            ventalinea = ventalineaform.save(commit=False)

        return HttpResponseRedirect('/sales/venta/')
