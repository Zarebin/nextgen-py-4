from django.contrib.auth.models import User
import math

def update_scores(user):
    user.score += 1
    user.level = math.floor(math.sqrt(user.score))
    user.save()
