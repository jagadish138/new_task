import django.forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class newform(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()



    # def password_clean(self):
    #     password1 =self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #
    #     if password1 and password2 and password1!=password2:
    #         raise ValidationError("password are not same")
    #     else:
    #         return password1
    #
    # def save(self, commit=True):
    #     user=User.objects.create_user(self.cleaned_data['username'],self.cleaned_data['password1'],self.cleaned_data['email'])
    #
    #     return user

