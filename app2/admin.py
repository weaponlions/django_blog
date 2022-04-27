from django.contrib import admin
from .models import MyModels
# Register your models here.

@admin.register(MyModels)
class MyModelsAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
