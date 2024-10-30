from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_image', 'full_name', 'cohort', 'program', 'status', 'date_joined', 'rating']
