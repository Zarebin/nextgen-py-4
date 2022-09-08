from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    score = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)
