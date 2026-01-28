from django.urls import path
from .views import GrowthView, GrowthDeleteView, GrowthUpdateView, GrowthCompleteView, GrowthUpdateCompleteView, GrowthDeleteCompleteView

app_name = 'growthapp'

urlpatterns = [
    path("growth/", GrowthView.as_view(), name="growth"),
    path("growth/delete/<int:pk>/", GrowthDeleteView.as_view(), name="growth_delete"),
    path("growth/update/<int:pk>/", GrowthUpdateView.as_view(), name="growth_update"),
    path("growth/complete/", GrowthCompleteView.as_view(), name="growth_complete"),
    path("growth/update/complete/", GrowthUpdateCompleteView.as_view(), name="growth_update_complete"),
    path("growth/delete/complete/", GrowthDeleteCompleteView.as_view(), name="growth_delete_complete"),
]
