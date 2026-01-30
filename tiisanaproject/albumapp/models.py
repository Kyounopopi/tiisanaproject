from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Album(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="albums"
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(
        Album,
        related_name="photos",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="photos/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.album.name} の写真"
