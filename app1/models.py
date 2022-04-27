from django.db import models

# Create your models here.

class MyModel(models.Model):
    first = models.CharField(null=True, blank=False, verbose_name='First Name', max_length=50, help_text='This is First Name')
    last = models.CharField(null=True, blank=False, verbose_name='Last Name', max_length=50, help_text='This is Last Name')
    age = models.IntegerField(null=True, blank=False, verbose_name='Age', help_text='This is Age')