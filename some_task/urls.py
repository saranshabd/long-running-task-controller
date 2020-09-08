"""
some_task app-level URL definitions
"""

from django.urls import path, include
from rest_framework import routers

from some_task import views

router = routers.DefaultRouter()
router.register("", views.GenericTaskControllerViewSet)

overall_router = routers.DefaultRouter()
overall_router.register("", views.OverallTaskControllerViewSet)

urlpatterns = [
  path("task_controller/", include(router.urls)),
  path("overall/", include(overall_router.urls))
]
