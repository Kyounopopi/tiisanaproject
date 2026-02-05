from django.db import models
from django.conf import settings

class Album(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

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
