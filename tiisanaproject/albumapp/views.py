from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Album, Photo
from .forms import AlbumCreateForm, PhotoCreateForm

from django.utils.text import slugify

import logging

logger = logging.getLogger(__name__)

class AlbumCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            "album_create.html",
            {
                "album_form": AlbumCreateForm(),
                "photo_form": PhotoCreateForm(),
            }
        )

    def post(self, request):
        album_form = AlbumCreateForm(request.POST)
        photo_form = PhotoCreateForm(request.POST, request.FILES)

        if album_form.is_valid() and photo_form.is_valid():
            album = album_form.save(commit=False)
            album.user = request.user
            album.slug = slugify(album.name)
            album.save()

            images = request.FILES.getlist("images")
            for image in images:
                Photo.objects.create(
                    album=album,
                    image=image
                )

            return redirect("albumapp:album_list")

        return render(
            request,
            "album_create.html",
            {
                "album_form": album_form,
                "photo_form": photo_form,
            }
        )


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
        return Album.objects.all()


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = "album_detail.html"
    context_object_name = "album"
    slug_field = "slug"
    slug_url_kwarg = "slug"


