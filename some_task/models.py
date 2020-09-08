"""
Database schemas of "some_task" app
"""

from uuid import uuid4
from django.db import models

STATUSES = (
    ("INIT", "INIT"),
    ("RUN", "RUN"),
    ("SUSPEND", "SUSPEND"),
    ("TERMINATE", "TERMINATE"),
)

class TaskStatusController(models.Model):
    """
    Database schema to store long-running tasks state data
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    desired_status = models.CharField(max_length=10, default="RUN", choices=STATUSES)
    current_status = models.CharField(max_length=10, default="INIT", choices=STATUSES)
