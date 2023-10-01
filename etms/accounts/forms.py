import django.forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class newform(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()



class loginForm(forms.Form):
    employeeName = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

