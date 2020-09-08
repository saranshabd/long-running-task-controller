"""
Long running tasks controllers
"""

import logging
import time
import threading

from task_controller import constants as task_controller_constants
from task_controller.controllers import TaskStatusControllerMaster

LOG = logging.getLogger(__name__)


class SampleControllerMaster(TaskStatusControllerMaster):
    """
    Controller master of a sample long-running task. There are no actual operations being
    performed by this controller master, instead running method just goes to sleep for a
    certain amout of time.
    """

    def __init__(self):
        super().__init__()
        self.counter = 10

    def start_sample_process(self):
        """
        Method to initiate the sample process. This method will create a new task record in
        database and set the ``current_state`` to running once the initialization process is
        completed.
        """

        self.perform_initialization()

        """
        @TODO
        ideal implementation of a long-running background process would be using Celery, but
        here since this is just a sample implementation we are going to use threads.
        """
        new_thread = threading.Thread(target=self.run_sample_process)
        new_thread.start()

        return self.task_id

    def run_sample_process(self):
        """
        Perform batch operations after verifying status of the task
        """

        counter = self.next_batch()
        while counter > 0:

            was_suspended = False

            if self.task_desired_status == task_controller_constants.SUSPEND_TASK_STATUS:
                was_suspended = True

                self.perform_cleanup()
                self.suspend_task()

                while self.task_desired_status == task_controller_constants.SUSPEND_TASK_STATUS:
                    time.sleep(3)

            if self.task_desired_status == task_controller_constants.TERMINATE_TASK_STATUS:
                self.perform_cleanup()
                self.terminate_task()
                return

            if was_suspended:
                self.resume_task()

            self.run_single_sample_process()
            counter = self.next_batch()

        self.perform_cleanup()
        self.terminate_task()

    def next_batch(self):
        """
        Check if there exists another batch to be performed, if so then return the counter
        """
        counter = self.counter
        self.counter -= 1
        return counter

    def run_single_sample_process(self):
        """
        Perform the actual batch task operation
        """
        time.sleep(10)

    def perform_initialization(self):
        """
        Perform initialization of the task
        """
        self.init_task()
        self.start_task()

    def perform_cleanup(self):
        """
        Perform clean up operation before terminating the task
        """
        time.sleep(2)
