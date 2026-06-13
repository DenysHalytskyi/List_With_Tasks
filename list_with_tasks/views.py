from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from list_with_tasks.models import Task, Tag
from list_with_tasks.forms import TaskForm


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    ordering = ["is_complete", "-created_at"]

class TagListView(ListView):
    model = Tag
    context_object_name = "tags"


def task_status(request, id) -> HttpResponse:
    task = Task.objects.get(id=id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect("list_with_tasks:task-list")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "list_with_tasks/task_form.html"
    success_url = reverse_lazy("list_with_tasks:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "list_with_tasks/task_form.html"
    success_url = reverse_lazy("list_with_tasks:task-list")


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("list_with_tasks:task-list")


class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    context_object_name = "tags"
    template_name = "list_with_tasks/tag_form.html"
    success_url = reverse_lazy("list_with_tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    context_object_name = "tags"
    template_name = "list_with_tasks/tag_form.html"
    success_url = reverse_lazy("list_with_tasks:tag-list")



def tag_delete(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return redirect("list_with_tasks:tag-list")

