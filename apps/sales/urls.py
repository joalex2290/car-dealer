from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
	url(r'^venta/add/', views.VentaCreateView.as_view(), name='add_venta'),
)