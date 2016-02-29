from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, View, ListView, CreateView, DetailView
from django.contrib.auth.models import User
from models import Reparacion, ReparacionLinea
from forms import ReparacionForm, ReparacionLineaForm, ReparacionLineaFormset

# Create your views here.

class ReparacionListView(ListView):
    model = Reparacion
    template_name = 'workshop/reparacion/show.html' 

    def get_queryset(self):
        return Reparacion.objects.all() 

class ReparacionLineaListView(ListView):
    model = ReparacionLinea
    template_name = 'workshop/reparacion/edit.html' 

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(ReparacionLineaListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return ReparacionLinea.objects.filter(id_reparacion=self.item_id) 

class ReparacionCreateView(TemplateView):
    reparacionform = ReparacionForm(prefix='reparacion')
    reparacionlineaform = ReparacionLineaForm(prefix='reparacion_linea')
    template_name = 'workshop/reparacion/add.html'

    def get_context_data(self, **kwargs):
        context = super(ReparacionCreateView, self).get_context_data(**kwargs)
        if 'reparacionform' not in context:
            context['reparacionform'] = self.reparacionform
        if 'reparacionlineaform' not in context:
            context['reparacionlineaform'] = self.reparacionlineaform
        if 'reparacionlineaformset' not in context:
            context['reparacionlineaformset'] = ReparacionLineaFormset
        try:
            reparacion = Reparacion.objects.latest('id_reparacion')
            context['cod'] = Reparacion.id_reparacion + 1
        except:
            context['cod'] = 1
        return context

    def post(self, request,*args,**kwargs):
        reparacionform = ReparacionForm(request.POST, prefix='reparacion')
        lineasformset = ReparacionLineaFormset(request.POST)
        if reparacionform.is_valid() & lineasformset.is_valid():
            reparacion = reparacionform.save(commit=False)
            reparacion.save()
            for form in lineasformset.forms:
                todo_item = form.save(commit=False)
                todo_item.id_reparacion = reparacion
                todo_item.save() 
        return HttpResponseRedirect('/workshop/reparaciones/')