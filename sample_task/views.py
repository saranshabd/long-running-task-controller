"""
API views of ``sample_task`` app
"""

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from sample_task.tasks import SampleControllerMaster


class SampleTaskViewSet(APIView):
    """
    API ViewSet of Sample Task Controller Master
    """

    def post(self, *args, **kwargs):
        """
        API endpoint to start a new background process, and get the task Id to control the
        task using task_controller API
        """

        new_task = SampleControllerMaster()
        task_id = new_task.start_sample_process()

        return Response(status=status.HTTP_201_CREATED, data={'task_id': task_id})
