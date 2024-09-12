from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache

# Create your views here.

PREDEFINED_USERNAME = 'mijwad'
PREDEFINED_PASSWORD = 'AlifLamMeem'
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
            request.session["logged_in"] = True
            return redirect(reverse('login:home'))
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login/login.html')

def default_redirect(request):
    if request.session.get('logged_in'):
        return redirect(reverse('login:home'))
    return redirect(reverse('login:login'))

@never_cache
def home(request):
    if not request.session.get('logged_in'):
        return redirect(reverse('login:login'))

    return render(request, 'login/home.html')

def signout(request):
    request.session.flush()
    return redirect(reverse('login:login'))
