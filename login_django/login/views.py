from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login:home')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login/login.html')

@never_cache
def home(request):
    if not request.user.is_authenticated:
        return redirect('login:login')
    return render(request, 'login/home.html')

def signout_view(request):
    logout(request)
    return redirect('login:login')