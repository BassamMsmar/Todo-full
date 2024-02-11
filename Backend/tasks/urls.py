from django.urls import path

from .api import TaskListApi

urlpatterns = [
    path('', TaskListApi.as_view(), name='list_task_api'),
]