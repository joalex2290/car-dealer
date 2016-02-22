from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, View, ListView, CreateView
from django.contrib.auth.models import User
from models import Cliente, Venta, VentaLinea
from forms import VentasForm, VentasLineaForm
from django.forms.formsets import formset_factory

# Create your views here.

class VentaCreateView(TemplateView):
    ventaform = VentasForm(prefix='venta')
    ventalineaform = VentasLineaForm(prefix='venta_linea')
    template_name = 'sales/venta/add.html'
    VentaLineaFormset = formset_factory(VentasLineaForm)

    def get_context_data(self, **kwargs):
        context = super(VentaCreateView, self).get_context_data(**kwargs)
        if 'ventaform' not in context:
            context['ventaform'] = self.ventaform
        if 'ventalineaform' not in context:
            context['ventalineaform'] = self.ventalineaform
        if 'ventalineaformset' not in context:
            context['ventalineaformset'] = self.VentaLineaFormset
        try:
            venta = Venta.objects.latest('id_venta')
            context['cod'] = venta.id_venta
        except:
            context['cod'] = 1
        return context

    def post(self, request,*args,**kwargs):
        ventasform = VentasForm(request.POST, prefix='venta')
        lineasformset = VentaLineaFormset(request.POST)
        if ventasform.is_valid() and lineasformset.is_valid():

            ventasform.save(commit=False)
            lineasformset.save(commit=False)

        return HttpResponseRedirect('/sales/venta/')
