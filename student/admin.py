from django.contrib import admin

# Register your models here.
from .models import StudentProfile,StudentDocuments

admin.site.register(StudentProfile)
admin.site.register(StudentDocuments)