from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

# Register the Student model with the admin interface
admin.site.register(Student)
