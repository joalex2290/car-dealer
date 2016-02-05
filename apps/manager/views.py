from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, View, ListView, CreateView
from django.contrib.auth.models import User
from models import Perfil, Sucursal, Fabricante
from forms import UserForm, UserPassForm, PerfilForm, SucursalForm, FabricanteForm

# Create your views here.

# Vistas Gestion Usuarios

class UserListView(ListView):
    model = User
    template_name = 'manager/users/show.html'

class UserCreateView(CreateView):
    model = Perfil
    userform = UserForm(prefix='user')
    perfilform = PerfilForm(prefix='perfil')
    template_name = 'manager/users/add.html'
    success_url = '/manager/users/'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['perfilform'] = self.perfilform
        context['userform'] = self.userform
        return context

    def form_valid(self, perfilform):
        self.object = perfilform.save()
        return render(self.request, 'manager/users/show.html', {'news': self.object})

class PerfilUpdateView(UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'manager/users/edit.html'

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(PerfilUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'success.html')

class ChangeUserPassword(TemplateView):
    template_name = 'manager/users/change-password.html'
    form_class = UserPassForm

    def post(self, request,**kwargs):
        form = UserPassForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=self.kwargs['pk'])
            user.set_password(form.cleaned_data['password'])
            user.save()
        return HttpResponseRedirect('/manager/users/')

    def get(self, request,**kwargs):
        context = self.get_context_data(object=User.objects.get(id=self.kwargs['pk']),form=self.form_class)
        return self.render_to_response(context)


class OnOffUser(View):

    def get(self, request,**kwargs):
        user = User.objects.get(id=self.kwargs['pk'])
        if user.is_active:
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()

        return HttpResponseRedirect('/manager/users/')

# Vistas Gestion Sucursales

class SucursalesListView(ListView):
    model = Sucursal
    template_name = 'manager/sucursales/show.html' 

    def get_queryset(self):
        return Sucursal.objects.all()  

class SucursalCreateView(CreateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'manager/sucursales/add.html'

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'success.html')

class SucursalUpdateView(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'manager/sucursales/edit.html'

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(SucursalUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'success.html')


# Vistas Gestion Marcas

class FabricanteListView(ListView):
    model = Fabricante
    template_name = 'manager/fabricantes/show.html' 

    def get_queryset(self):
        return Fabricante.objects.all()  

class FabricanteCreateView(CreateView):
    model = Fabricante
    form_class = FabricanteForm
    template_name = 'manager/fabricantes/add.html'

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'success.html')

class FabricanteUpdateView(UpdateView):
    model = Fabricante
    form_class = FabricanteForm
    template_name = 'manager/fabricantes/edit.html'

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(FabricanteUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'success.html')

class OnOffFabricante(View):

    def get(self, request,**kwargs):
        fabricante = Fabricante.objects.get(id=self.kwargs['pk'])
        if fabricante.is_active:
            fabricante.is_active = False
            fabricante.save()
        else:
            fabricante.is_active = True
            fabricante.save()

        return HttpResponseRedirect('/manager/fabricantes/')
