from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In !!!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password !!!")
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have Successfully Logout...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})

