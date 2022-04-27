from django.contrib import admin
from .models import ModeUser, ModeUser2
# Register your models here.
@admin.register(ModeUser)
class ModeUserAdmin(admin.ModelAdmin):
    list_display = ('usere', 'address', 'date')
    


@admin.register(ModeUser2)
class ModeUser2Admin(admin.ModelAdmin):
    list_display = ('usere', 'address2', 'date')
