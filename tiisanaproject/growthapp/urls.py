from django.urls import path
from .views import GrowthView, GrowthDeleteView, GrowthUpdateView

app_name = 'growthapp'

urlpatterns = [
    path("growth/", GrowthView.as_view(), name="growth"),
    path("growth/delete/<int:pk>/", GrowthDeleteView.as_view(), name="growth_delete"),
    path("growth/update/<int:pk>/", GrowthUpdateView.as_view(), name="growth_update"),
]
