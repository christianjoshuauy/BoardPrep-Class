from django import forms

from .models import Specialization


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(max_length=255, label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    user_name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=255, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    specialization = forms.ChoiceField(choices=Specialization.CHOICES, label='', widget=forms.Select(attrs={'placeholder': 'Select Specialization'}))


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=255, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))