"""
URL definitions of ``task_definition`` app-level
"""

from django.urls import path, include
from rest_framework import routers

from task_controller import views

router = routers.DefaultRouter()
router.register("", views.TaskControllerViewSet)

urlpatterns = [
  path("", include(router.urls))
]
