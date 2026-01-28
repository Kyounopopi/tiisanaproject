from django.urls import path
from . import views

app_name = "photoapp"

urlpatterns = [
    path("", views.photo_list, name="list"),
]
