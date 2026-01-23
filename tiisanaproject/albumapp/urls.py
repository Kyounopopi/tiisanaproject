from django.urls import path
from .views import (
    AlbumListView,
    AlbumCreateView,
    AlbumDetailView,
    ToggleFavoriteView,
)

app_name = "albumapp"

urlpatterns = [
    path("home/album/", AlbumListView.as_view(), name="album_list"),
    path("home/album/create/", AlbumCreateView.as_view(), name="album_create"),
    path("home/album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("home/album/favorite/<int:photo_id>/", ToggleFavoriteView.as_view(), name="toggle_favorite"),
]
