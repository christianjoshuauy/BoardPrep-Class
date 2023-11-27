from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Specialization, Teacher
from django.utils import timezone


# Create your views here.
def login(request):
    error_message = None
    if request.method == 'POST':
        if 'register' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                name = first_name + " " + last_name
                user_name = form.cleaned_data['user_name']
                password = make_password(form.cleaned_data['password'])
                email = form.cleaned_data['email']
                specialization_id = form.cleaned_data['specialization']

                try:
                    teacher = Teacher.objects.get(email=email)
                    error_message = "Email already exists"
                except Teacher.DoesNotExist:
                    try:
                        teacher = Teacher.objects.get(user_name=user_name)
                        error_message = "Username already taken"
                    except Teacher.DoesNotExist:
                        specialization = Specialization.objects.get(id=specialization_id)

                        new_student = Teacher(
                            name=name,
                            user_name=user_name,
                            password=password,
                            email=email,
                            specialization=specialization,
                        )
                        new_student.save()
                        request.session['username'] = user_name
                        return redirect('class')
        elif 'login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['user_name']
                password = form.cleaned_data['password']

                try:
                    teacher = Teacher.objects.get(user_name=username)
                    if check_password(password, teacher.password):
                        teacher.last_login = timezone.now()
                        teacher.save()
                        request.session['username'] = username
                        return redirect('class')
                    else:
                        error_message = "Incorrect Password"
                except Teacher.DoesNotExist:
                    error_message = "User not found"

    else:
        form = RegisterForm()

    return render(request, 'login.html', {'register_form': RegisterForm(), 'login_form': LoginForm(),
                                          'error_message': error_message})

def index(request):
    return render(request, 'index.html')
