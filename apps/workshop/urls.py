from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
	url(r'^reparaciones/', views.ReparacionListView.as_view(), name='show_reparacion'),
	url(r'^reparacion/add/', views.ReparacionCreateView.as_view(), name='create_reparacion'),
    url(r'^reparacion/detail/(?P<pk>[-\w]+)/', views.ReparacionLineaListView.as_view(), name="show_lineas_reparaciones"),
)