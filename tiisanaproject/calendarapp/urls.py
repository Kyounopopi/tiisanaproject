from django.urls import path
from . import views

app_name = 'calendarapp'

urlpatterns = [
    path('currender/', views.calendar_view, name='currender'),
]