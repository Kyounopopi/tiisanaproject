from django.urls import path
from .views import (
    PhotoListView, 
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView
)

app_name = "photoapp"

urlpatterns = [
    path("photo/", PhotoListView.as_view(), name="photo_list"),
    path("photo/create/", PhotoCreateView.as_view(), name="photo_create"),
    path("photo/<int:pk>/", PhotoDetailView.as_view(), name="photo_detail"),
    path("photo/<int:pk>/update/", PhotoUpdateView.as_view(), name="photo_update"),
    path("photo/<int:pk>/delete/", PhotoDeleteView.as_view(), name="photo_delete"),
]