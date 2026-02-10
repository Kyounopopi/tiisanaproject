from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "albumapp"

urlpatterns = [
    path("album/", views.AlbumListView.as_view(), name="album_list"),
    path("create/", views.AlbumCreateView.as_view(), name="album_create"),
    path("<int:pk>/", views.AlbumDetailView.as_view() ,name="album_detail"),
    path("favorite/<int:photo_id>/", views.ToggleFavoriteView.as_view(), name="toggle_favorite"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

