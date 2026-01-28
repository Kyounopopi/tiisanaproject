from django.urls import path
from .views import (
    AlbumListView,
    AlbumCreateView,
    AlbumDetailView,
    ToggleFavoriteView,
)

app_name = "albumapp"

urlpatterns = [
    path("album", AlbumListView.as_view(), name="album_list"),
    path("create/", AlbumCreateView.as_view(), name="album_create"),
    path("<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("favorite/<int:photo_id>/", ToggleFavoriteView.as_view(), name="toggle_favorite"),
]
