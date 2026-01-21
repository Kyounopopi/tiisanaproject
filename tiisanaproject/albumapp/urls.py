from django.urls import path
from . import views

app_name = 'albumapp'

urlpatterns = [
    path("create/", views.AlbumCreateView.as_view(), name="album_create"),
    path("favorite/<int:photo_id>/", views.ToggleFavoriteView.as_view(), name="toggle_favorite"),
]
