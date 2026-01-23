from django.urls import path
from . import views

app_name = 'calendarapp'

urlpatterns = [
    path('currender/', views.calendar_view, name='currender'),
    path('add/', views.add_record, name='add_record'),
    path("comment/<int:record_id>/", views.edit_comment, name="edit_comment"),
]