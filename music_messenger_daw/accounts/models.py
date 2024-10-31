# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    STATUS_CHOICES = [
        ('artist', 'Артист'),
        ('musician', 'Музыкант'),
        ('producer', 'Продюсер'),
        ('beatmaker', 'Битмейкер'),
        # Добавьте другие статусы по мере необходимости
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='musician')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    # Добавьте другие поля по мере необходимости
