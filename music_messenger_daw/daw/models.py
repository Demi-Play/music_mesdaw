from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tracks = models.JSONField(default=list)  # Список треков и их настройки
    mixer_settings = models.JSONField(default=dict)  # Настройки микшера
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
