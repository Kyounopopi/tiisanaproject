from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
from .models import Album, Photo
from .forms import AlbumCreateForm, PhotoUploadForm
import logging

logger = logging.getLogger(__name__)


class AlbumCreateView(View):
    template_name = "album_create.html"

    def get(self, request):
        return self.render_forms()

    def post(self, request):
        album_form = AlbumCreateForm(request.POST)
        photo_form = PhotoUploadForm(request.POST, request.FILES)

        if not album_form.is_valid():
            logger.warning("Album form invalid")
            return self.render_forms(album_form, photo_form)

        if not photo_form.is_valid():
            logger.warning("Photo form invalid")
            return self.render_forms(album_form, photo_form)

        try:
            self.save_album_and_photos(
                album_form,
                request.FILES.getlist("images")
            )
        except Exception as e:
            logger.error("Save failed", exc_info=e)
            return self.render_forms(album_form, photo_form)

        return redirect("album_list")

    # ---------- 以下、責務ごとのメソッド ----------

    def render_forms(self, album_form=None, photo_form=None):
        return render(
            self.request,
            self.template_name,
            {
                "album_form": album_form or AlbumCreateForm(),
                "photo_form": photo_form or PhotoUploadForm(),
            }
        )

    @transaction.atomic
    def save_album_and_photos(self, album_form, images):
        logger.info("Saving album")
        album = album_form.save()

        logger.info(f"Saving {len(images)} photos")
        for image in images:
            Photo.objects.create(
                album=album,
                image=image
            )

class ToggleFavoriteView(View):
    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        photo.is_favorite = not photo.is_favorite
        photo.save()
        return redirect("album_detail", album_id=photo.album.id)
