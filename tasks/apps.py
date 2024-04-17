from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=200, default="")
    is_done = models.BooleanField(default=False)