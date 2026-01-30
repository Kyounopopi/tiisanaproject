from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Album, Photo
from .forms import AlbumCreateForm

import logging

logger = logging.getLogger(__name__)


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ["name"]
    template_name = "album_create.html"
    success_url = "/album/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PhotoCreateView(LoginRequiredMixin, View):
    def post(self, request, slug):
        album = get_object_or_404(Album, slug=slug, user=request.user)

        images = request.FILES.getlist("images")
        for image in images:
            Photo.objects.create(album=album, image=image)

        return redirect("albumapp:album_detail", slug=album.slug)

class ToggleFavoriteView(View):
    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        photo.is_favorite = not photo.is_favorite
        photo.save()
        return redirect("album_detail", pk=photo.album.id)


class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = "album_list.html"
    context_object_name = "albums"

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = "album_detail.html"
    context_object_name = "album"
    slug_field = "slug"
    slug_url_kwarg = "slug"


