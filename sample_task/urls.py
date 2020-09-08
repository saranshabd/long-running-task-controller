"""
URL definitions of ``sample_task`` app-level
"""

from django.urls import path

from sample_task import views

urlpatterns = [
  path("start/", views.SampleTaskViewSet.as_view())
]
