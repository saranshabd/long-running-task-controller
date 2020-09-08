"""
Database schemas of "some_task" app
"""

from uuid import uuid4
from django.db import models
from task_controller import constants

STATUSES = (
    (constants.INIT_TASK_STATUS, constants.INIT_TASK_STATUS),
    (constants.RUN_TASK_STATUS, constants.RUN_TASK_STATUS),
    (constants.SUSPEND_TASK_STATUS, constants.SUSPEND_TASK_STATUS),
    (constants.TERMINATE_TASK_STATUS, constants.TERMINATE_TASK_STATUS),
)

class TaskStatusController(models.Model):
    """
    Database schema to store long-running tasks state data
    """

    id = models.UUIDField(primary_key=True, default=uuid4)

    desired_status = models.CharField(max_length=10,
                                      default=constants.RUN_TASK_STATUS,
                                      choices=STATUSES)

    current_status = models.CharField(max_length=10,
                                      default=constants.INIT_TASK_STATUS,
                                      choices=STATUSES)
