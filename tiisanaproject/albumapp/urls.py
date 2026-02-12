from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "albumapp"

urlpatterns = [
    path("album/", views.AlbumListView.as_view(), name="album_list"),
    path("album/create/", views.AlbumCreateView.as_view(), name="album_create"),
    path("album/<int:pk>/", views.AlbumDetailView.as_view() ,name="album_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

