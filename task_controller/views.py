"""
API views of ``task_controller`` app
"""

from rest_framework import status
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from task_controller.models import TaskStatusController
from task_controller import constants
from task_controller.serializers import (TaskStatusControllerSerializer,
                                   UpdateTaskStatusControllerSerializer)


class TaskControllerViewSet(mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """
    Task controller API to set the status of any long-running task
    """

    queryset = TaskStatusController.objects.all()
    serializer_class = TaskStatusControllerSerializer

    def update(self, request, pk=None): # pylint: disable=invalid-name
        """
        Update ``desired_status`` of task controller of a particular task
        """

        instance = self.get_object()
        serializer = UpdateTaskStatusControllerSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        task_controller = TaskStatusController.objects.get(id=pk)
        if task_controller.current_status == constants.TERMINATE_TASK_STATUS:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                "detail": "Operation cannot be performed on terminated task."
            })

        serializer.save()

        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="filter")
    def get_filtered(self, request):
        """
        Get filtered task controller statuses from database. Filter can only be applied
        on ``desired_status`` or ``current_status``.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        queryset = self.get_queryset()
        if validated_data.get("current_status") is not None:
            queryset = queryset.filter(current_status=validated_data.get("current_status"))
        if validated_data.get("desired_status") is not None:
            queryset = queryset.filter(desired_status=validated_data.get("desired_status"))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
