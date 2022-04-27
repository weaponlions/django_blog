from django.db import models

# Create your models here.

class MyModels(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField( null=True)