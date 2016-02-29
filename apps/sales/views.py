from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, View, ListView, CreateView, DetailView
from django.contrib.auth.models import User
from models import Cliente, Venta, VentaLinea
from forms import VentasForm, VentasLineaForm, VentaLineaFormset

# Create your views here.

class VentasListView(ListView):
    model = Venta
    template_name = 'sales/venta/show.html' 

    def get_queryset(self):
        return Venta.objects.all() 

class VentaLineaListView(ListView):
    model = VentaLinea
    template_name = 'sales/venta/edit.html' 

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(VentaLineaListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return VentaLinea.objects.filter(id_venta=self.item_id) 

class VentaCreateView(TemplateView):
    ventaform = VentasForm(prefix='venta')
    ventalineaform = VentasLineaForm(prefix='venta_linea')
    template_name = 'sales/venta/add.html'

    def get_context_data(self, **kwargs):
        context = super(VentaCreateView, self).get_context_data(**kwargs)
        if 'ventaform' not in context:
            context['ventaform'] = self.ventaform
        if 'ventalineaform' not in context:
            context['ventalineaform'] = self.ventalineaform
        if 'ventalineaformset' not in context:
            context['ventalineaformset'] = VentaLineaFormset
        try:
            venta = Venta.objects.latest('id_venta')
            context['cod'] = venta.id_venta + 1
        except:
            context['cod'] = 1
        return context

    def post(self, request,*args,**kwargs):
        ventasform = VentasForm(request.POST, prefix='venta')
        lineasformset = VentaLineaFormset(request.POST)
        if ventasform.is_valid() & lineasformset.is_valid():
            ventas = ventasform.save(commit=False)
            ventas.save()
            for form in lineasformset.forms:
                todo_item = form.save(commit=False)
                todo_item.id_venta = ventas
                todo_item.save() 
        return HttpResponseRedirect('/sales/ventas/')

class ClientesListView(ListView):
    model = Cliente
    template_name = 'sales/clientes/show.html' 

    def get_queryset(self):
        return Cliente.objects.all()  

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'sales/clientes/add.html'

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'success.html')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'sales/clientes/edit.html'

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(ClienteUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'success.html')