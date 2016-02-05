from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, View, ListView, CreateView
from .forms import ArticuloForm
from models import Articulo

# Create your views here.

# Vistas Gestion Articulos

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'inventory/articulos/show.html' 

    def get_queryset(self):
        return Articulo.objects.all()  

class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'inventory/articulos/add.html'

class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'inventory/articulos/edit.html'
    success_url = "/inventory/articulos/"

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(ArticuloUpdateView, self).dispatch(*args, **kwargs)

class OnOffArticulo(View):

    def get(self, request,**kwargs):
        articulo = Articulo.objects.get(id=self.kwargs['pk'])
        if articulo.is_active:
            articulo.is_active = False
            articulo.save()
        else:
            articulo.is_active = True
            articulo.save()

        return HttpResponseRedirect('/inventory/articulos/')

class Success(View):
    template_name = 'inventory/articulos/success.html'