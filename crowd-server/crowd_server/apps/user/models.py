from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    