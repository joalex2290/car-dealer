from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
	url(r'^/', views.ConsultView.as_view(), name='consult'),
	url(r'^result/(?P<pk>[-\w]+)/', views.ResultConsultView.as_view(), name='consult_result'),
)