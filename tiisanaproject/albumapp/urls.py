from django.urls import path
from . import views

app_name = 'albumapp'

urlpatterns = [
    path('album/', views.AlbumView.as_view(), name='album'),
    
    path('home/', views.HomeView.as_view(), name='home'),
    
]