from rest_framework import generics
from .serializer import TaskSerializer

from .models import Task

class TaskListApi(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer