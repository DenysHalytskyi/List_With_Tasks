from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    tags = models.ManyToManyField("Tag", related_name='tasks')

    def __str__(self):
        return f"{self.content} - {self.deadline}"


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"
