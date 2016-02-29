from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView, View, ListView, CreateView
from apps.sales.models import Venta

# Create your views here.

class ConsultView(TemplateView):
	template_name = 'consult.html'

class ResultConsultView(TemplateView):
	template_name = 'consult.html'

