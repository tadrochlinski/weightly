from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    lifestyle = models.CharField(max_length=20, blank=True, null=True)
    goal = models.CharField(max_length=20, blank=True, null=True)