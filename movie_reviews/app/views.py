from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, Review
import datetime


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'app/home.html', context)

def details(request, pk):
    obj = Movie.objects.get(id=pk)
    queryset = Review.objects.filter(movie__id__icontains=pk).order_by('-date_added')

    context = {
        'obj': obj,
        'reviews': queryset,
    }

    return render(request, 'app/details.html', context)

def add_review(request, pk):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        movie_obj = Movie.objects.get(id=pk)
        Review.objects.create(review_title=title, content=content, movie=movie_obj)
        return HttpResponseRedirect('/')


    return render(request, 'app/add_review.html')