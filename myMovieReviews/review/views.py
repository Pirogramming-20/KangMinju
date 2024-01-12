from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.

def review_list(request):
    movies = Movie.objects.all()
    sort_by = request.GET.get('sort_by')
    
    if sort_by == 'rating':
        movies = sorted(movies, key=lambda movie: float(movie.rating), reverse=True) 
    elif sort_by == 'time':
        movies = sorted(movies, key=lambda movie: int(movie.time)) 
    elif sort_by == 'year':
        movies = sorted(movies, key=lambda movie: int(movie.year), reverse=True)   
    else:
        movies = movies.order_by('title')
    
    movie_durations = []
    for movie in movies:
        total_minutes = int(movie.time)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        movie_durations.append({"hours": hours, "minutes": minutes})
    info_list = zip(movies, movie_durations)
    context = {
        'info_list': info_list,
    }
    return render(request, 'review_list.html', context)

def review_read(request, pk):
    movie = Movie.objects.get(id=pk)
    total_minutes = int(movie.time)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    context = {
        "movie" : movie,
        "hours": hours,
        "minutes": minutes,
    }
    return render(request, "review_read.html", context)

def review_create(request):
    context = {
        'GENRE_CHOICES': Movie.GENRE_CHOICES,
    }
    if request.method == "POST":
        Movie.objects.create (
            title = request.POST["title"],
            year = request.POST["year"],
            genre = request.POST["genre"],
            rating = request.POST["rating"],
            time = request.POST["time"],
            review = request.POST["review"],
            director = request.POST["director"],
            actor = request.POST["actor"],
        )
        return redirect("/review")
    return render(request, "review_create.html", context)

def review_update(request, pk) :
    movie = Movie.objects.get(id=pk)
    context = {
        'GENRE_CHOICES': Movie.GENRE_CHOICES,
        "movie" : movie
    }
    if request.method == "POST" :
        movie.title = request.POST["title"]
        movie.year = request.POST["year"]
        movie.genre = request.POST["genre"]
        movie.rating = request.POST["rating"]
        movie.time = request.POST["time"]
        movie.review = request.POST["review"]
        movie.director = request.POST["director"]
        movie.actor = request.POST["actor"]
        movie.save()
        return redirect(f"/review/{pk}")
    return render(request, "review_update.html", context)

def review_delete (request, pk):
    if request.method == "POST":
        movie = Movie.objects.get(id = pk)
        movie.delete()
    return redirect("/review")
