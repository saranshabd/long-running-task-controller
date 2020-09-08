"""
Controller classes for real-time task management
"""

import logging

from task_controller.models import TaskStatusController
from task_controller import constants

LOG = logging.getLogger(__name__)


class TaskStatusControllerMaster:
    """
    Master controller of long-running tasks. All long-running task classes must inherit this
    class inorder to use of real-time task management.
    """

    def __init__(self):
        self.task_id = None

    def init_task(self):
        """
        Create a new task in the database. This method should be called before initializing
        a task.
        """
        task_controller = TaskStatusController.objects.create()
        self.task_id = task_controller.id
        LOG.debug("%s: initiated", self.task_id)

    def start_task(self):
        """
        Set current status of the task as running. This method should only be called once
        the task has been initialized and is about to be started.
        """
        task_controller = TaskStatusController.objects.filter(id=self.task_id)
        task_controller.update(current_status=constants.RUN_TASK_STATUS)
        LOG.debug("%s: started", self.task_id)

    def resume_task(self):
        """
        Set current status of the task as running. This method cannot  be called on a
        terminated task.
        """
        task_controller = TaskStatusController.objects.filter(id=self.task_id)
        if task_controller[0].current_status != constants.TERMINATE_TASK_STATUS:
            task_controller.update(current_status=constants.RUN_TASK_STATUS)
        LOG.debug("%s: resuming", self.task_id)

    def suspend_task(self):
        """
        Set current status of the task as suspended. This method should only be called after
        performing all the cleanup.
        """
        task_controller = TaskStatusController.objects.filter(id=self.task_id)
        task_controller.update(current_status=constants.SUSPEND_TASK_STATUS)
        LOG.debug("%s: suspended", self.task_id)

    def terminate_task(self):
        """
        Set current status of the task as terminated. This method should only be called after
        performing all the cleanup.
        """
        task_controller = TaskStatusController.objects.filter(id=self.task_id)
        task_controller.update(current_status=constants.TERMINATE_TASK_STATUS)
        LOG.debug("%s: terminated", self.task_id)

    @property
    def task_desired_status(self):
        """
        Task desired state set by the user in database
        """
        return TaskStatusController.objects.get(id=self.task_id).desired_status
