
from django.shortcuts import render
from .forms import newform
from django.contrib.auth.models import User
# Create your views here.

def login(request):
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