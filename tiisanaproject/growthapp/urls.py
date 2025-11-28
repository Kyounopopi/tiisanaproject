from django.urls import path
from .views import GrowthView

app_name = 'growthapp'

urlpatterns = [
    path("growth/", GrowthView.as_view(), name="growth"),
    
    # path('', views.GorwthView.as_view(), name='growth')
]
