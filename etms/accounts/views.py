
from django.shortcuts import render
from .forms import newform,loginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def Register(request):
    form = newform()
    if request.method == "POST":
        form = newform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pass1 = form.cleaned_data['password1']
            mail =  form.cleaned_data['email']

            new_user = User(username=username,password=pass1,email=mail)
            new_user.save()


    form = newform()
    return render(request, "Register.html", {"form": form})


def Login(request):
    new_user = loginForm()
    if request.method=='POST':
        new_user=loginForm(request.POST)
        if new_user.is_valid():
            name = new_user.cleaned_data['username']
            pass1 = new_user.cleaned_data['passowrd']

            user=authenticate(username=name,password=pass1)
            if user is not None:
                return render(request, "home.html")

    return render(request, "Login.html", {"form": new_user})


