from django.contrib import admin

from list_with_tasks.models import Task, Tag


class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "deadline", "is_complete"]
    list_filter = ["created_at", "deadline", "is_complete"]

admin.site.register(Task, TaskAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Tag, TagAdmin)

