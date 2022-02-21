from django.contrib import admin
from .models import AdviserProfile
# Register your models here.

class AdviserModel(admin.ModelAdmin):
    
    list_display = ['user', 'first_name', 'last_name', 'email']


admin.site.register(AdviserProfile, AdviserModel)