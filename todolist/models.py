from django.utils import timezone
from django.db import models
from django.contrib.auth import settings

class ToDoList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)