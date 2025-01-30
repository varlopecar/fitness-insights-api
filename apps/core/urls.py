app_name = "core"
from django.urls import path, include

urlpatterns = [
    path("", include("apps.health_tracker.urls")),
]
