from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ModeUser(models.Model):
    usere = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now=True, null=True)


class ModeUser2(models.Model):
    usere = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address2 = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)