from django.shortcuts import render
from datetime import date
import calendar
# Create your views here.

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name = 'home.html'