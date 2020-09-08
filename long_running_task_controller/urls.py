"""
Project-level URL definitions
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

SchemaView = get_schema_view(
   openapi.Info(
      title="Long running task controller API",
      default_version='v1',
      description=(
          "API to control long running backend tasks in real-time without"
          "breaking any business logicn"
      ),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_docs_urlpatterns = [
    path("swagger/", SchemaView.with_ui("swagger")),
    path("redoc/", SchemaView.with_ui("redoc")),
]

api_urlpatterns = [
    path("some_task/", include("some_task.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urlpatterns)),
    path("api/v1/docs/", include(api_docs_urlpatterns)),
]
