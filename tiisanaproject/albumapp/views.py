from django.shortcuts import render
from datetime import date
import calendar
# Create your views here.

from django.views.generic import TemplateView

class AlbumView(TemplateView):
    template_name = 'album.html'

class HomeView(TemplateView):
    template_name = 'home.html'