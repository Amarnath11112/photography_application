from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Photography

def home(request):
    pg=Photography.objects.all()
    return render(request, 'photography/home.html',{"pg":pg})


def about(request):
    return render(request, 'photography/about.html')

def contact(request):
    return render(request, 'photography/contact.html')

def stories(request):
    return render(request, 'photography/stories.html')

def films(request):
    pg_films = Photography.objects.all()
    return render(request, 'photography/films.html',{"pg_films":pg_films})



