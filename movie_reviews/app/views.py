from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'app/home.html', context)
