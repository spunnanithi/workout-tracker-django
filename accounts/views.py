from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from accounts.forms import *

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect("list_workouts")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("user_login")

def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                )
                login(request, user)
                return redirect("list_workouts")
            else:
                form.add_error("password", "The password does not match! Try again.")
    else:
        form = SignupForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
