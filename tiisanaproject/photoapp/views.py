from django.views.generic import ListView, DetailView
from .models import Photo

class PhotoListView(ListView):
    model = Photo
    template_name = "photoapp/photo_list.html"
    context_object_name = "photos"
    ordering = ["-id"]


class PhotoDetailView(DetailView):
    model = Photo
    template_name = "photoapp/photo_detail.html"
    context_object_name = "photo"
