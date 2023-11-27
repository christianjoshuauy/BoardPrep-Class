from django.shortcuts import render, redirect
from .forms import ClassForm
from User.models import Teacher
from .models import Class

# Create your views here.
def myClass(request):
    teacher_username = request.session.get('username', None)

    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            if teacher_username:
                teacher = Teacher.objects.get(user_name=teacher_username)
                new_class.teacher_id = teacher
            new_class.save()

            return redirect('class')
    else:
        form = ClassForm()

    if teacher_username:
        try:
            classes = Class.objects.filter(teacher_id=teacher_username)
        except Class.DoesNotExist:
            classes = []
    else:
        # Handle the case when the teacher's username is not found
        classes = []

    return render(request, 'index.html', {'classes': classes, 'form': form})
