from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',

    url(r'^users/', views.UserListView.as_view(), name='list_users'),
    url(r'^user/create/', views.UserCreateView.as_view(), name='create_user'),
    url(r'^user/edit/(?P<pk>[-\w]+)/', views.PerfilUpdateView.as_view(), name="edit_perfil"),
    url(r'^user/change-pass/(?P<pk>[-\w]+)/', views.ChangeUserPassword.as_view(), name="change_user_password"),
    url(r'^user/onoff/(?P<pk>[-\w]+)/', views.OnOffUser.as_view(), name="onoff_user"),

    url(r'^sucursales/', views.SucursalesListView.as_view(), name='show_sucursales'),
    url(r'^sucursal/create/', views.SucursalCreateView.as_view(), name='create_sucursal'),
    url(r'^sucursal/edit/(?P<pk>[-\w]+)/', views.SucursalUpdateView.as_view(), name="edit_sucursal"),

    url(r'^fabricantes/', views.FabricanteListView.as_view(), name='show_fabricantes'),
    url(r'^fabricante/create/', views.FabricanteCreateView.as_view(), name='create_fabricante'),
    url(r'^fabricante/edit/(?P<pk>[-\w]+)/', views.FabricanteUpdateView.as_view(), name='edit_fabricante'),
    url(r'^fabricante/onoff/(?P<pk>[-\w]+)/', views.OnOffFabricante.as_view(), name="onoff_fabricante"),
)