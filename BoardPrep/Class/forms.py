from django import forms
from .models import Class

class ClassForm(forms.ModelForm):
    className = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Class Name'}))
    classDescription = forms.CharField(max_length=255, label='', widget=forms.Textarea(attrs={'placeholder': 'Class '
                                                                                                       'Description'}))
    class Meta:
        model = Class
        fields = ['className', 'classDescription']