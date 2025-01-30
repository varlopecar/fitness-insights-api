from django.urls import path
from .views import HealthScoreView

urlpatterns = [
    path('healthScore/<str:user_id>/',
         HealthScoreView.as_view(), name='health_score'),
]
