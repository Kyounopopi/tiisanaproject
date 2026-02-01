from django.views.generic import ListView, DetailView
from .models import Photo

class PhotoListView(ListView):
    model = Photo
    template_name = "photo_list.html"
    context_object_name = "photo_list"

class PhotoDetailView(DetailView):
    model = Photo
    template_name = "photo_detail.html"
    context_object_name = "photo"
