"""
Database schema serializers of ``task_controller`` app
"""

from rest_framework import serializers

from task_controller.models import TaskStatusController


class TaskStatusControllerSerializer(serializers.ModelSerializer):
    """
    Serializer of `some_task.TaskStatusController` database schema
    """

    class Meta:
        model = TaskStatusController
        fields = ("id", "desired_status", "current_status",)


class UpdateTaskStatusControllerSerializer(serializers.ModelSerializer):
    """
    Serializer of `some_task.TaskStatusController` database schema to update
    ``desired_status`` property of a record
    """

    desired_status = serializers.CharField(required=True)

    class Meta:
        model = TaskStatusController
        fields = ("desired_status",)
