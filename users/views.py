from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "index.html")

def user_login(request):
    return render(request, "login.html")

def user_register(request):
    return render(request, "register.html")
