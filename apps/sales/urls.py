from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
	url(r'^ventas/', views.VentasListView.as_view(), name='show_venta'),
	url(r'^venta/add/', views.VentaCreateView.as_view(), name='create_venta'),
    url(r'^venta/detail/(?P<pk>[-\w]+)/', views.VentaLineaListView.as_view(), name="show_lineas_ventas"),

	url(r'^clientes/', views.ClientesListView.as_view(), name='show_clientes'),
    url(r'^cliente/create/', views.ClienteCreateView.as_view(), name='create_cliente'),
    url(r'^cliente/edit/(?P<pk>[-\w]+)/', views.ClienteUpdateView.as_view(), name="edit_cliente"),
)