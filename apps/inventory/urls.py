from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',

    url(r'^articulos/', views.ArticuloListView.as_view(), name='show_articulos'),
    url(r'^articulo/create/', views.ArticuloCreateView.as_view(), name='create_articulo'),
    url(r'^articulo/edit/(?P<pk>[-\w]+)/', views.ArticuloUpdateView.as_view(), name='edit_articulo'),
    url(r'^articulo/onoff/(?P<pk>[-\w]+)/', views.OnOffArticulo.as_view(), name="onoff_articulo"),
)