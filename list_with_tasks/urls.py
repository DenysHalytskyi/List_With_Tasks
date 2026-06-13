from django.urls import path
from list_with_tasks.views import (
    TaskListView,
    TagListView,
)


app_name = 'list_with_tasks'
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
