from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import PG_users


def home(request):
    return render(request, 'pg_users/home.html')

def signup_page(request):
    return render(request, 'pg_users/signup_page.html')

def login_page(request):
    return render(request, 'pg_users/login_page.html')

def authentication(username, password):
    try:
        user = PG_users.objects.get(username=username, password=password)
        return user
    except PG_users.DoesNotExist:
        user = None
        return user

def login(request):
    username = request.POST.get('uname')
    password = request.POST.get('psw')
    user_data=authentication(username, password)
    print(user_data)
    if user_data is not None:
        return render(request, 'pg_users/home.html', {'user_data':user_data})
    else:
        return render(request, 'pg_users/login_page.html')

def signup(request):
    username = request.GET['username']
    email = request.GET['email']
    password=request.GET['psw']
    password2 = request.GET['psw-repeat']
    user=PG_users.objects.create(username=username, email=email, password=password)
    if user is not None:
        data = {'username': username, 'email': email, 'password': password}
        authentication(username, password)
        return render(request, 'pg_users/home.html', {'data': data})
    else:
        return render(request, 'pg_users/signup_page.html')






