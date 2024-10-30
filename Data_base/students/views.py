from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_dashboard(request):
    students = Student.objects.all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    else:
        form = StudentForm()

    return render(request, 'students/index.html', {'form': form, 'students': students})
