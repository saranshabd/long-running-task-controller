"""
Database schema serializers of "some_task" app
"""

from rest_framework import serializers

from some_task.models import TaskStatusController


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
