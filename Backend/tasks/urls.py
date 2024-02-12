from django.urls import path

from .api import TaskListApi, TaskDetailApi

urlpatterns = [
    path('tasks/api/', TaskListApi.as_view(), name='list_task_api'),
    path('tasks/api/<int:pk>/', TaskDetailApi.as_view(), name='detail_task_api'),
]