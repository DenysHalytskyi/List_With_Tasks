from django.urls import path
from list_with_tasks.views import (
    TaskListView,
    TagListView,
    task_status,
    TaskCreateView,
    TaskUpdateView,
)


app_name = 'list_with_tasks'
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:id>/toggle/", task_status, name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tag-list"),

    path("tasks/create/", TaskCreateView.as_view(), name="task-form"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-form"),
]
