from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
def review_list(request):
    movies = Movie.objects.all()
    context = {
        "movies" : movies
    }
    return render(request, 'review_list.html', context)

def review_read(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {
        "movie" : movie
    }
    return render(request, "review_read.html", context)

def review_create(request):
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
    return render(request, "review_create.html")

def review_update(request, pk) :
    movie = Movie.objects.get(id=pk)
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
    context = {
        "movie" : movie
    }
    return render(request, "review_update.html", context)

def review_delete (request, pk):
    if request.method == "POST":
        movie = Movie.objects.get(id = pk)
        movie.delete()
    return redirect("/review")
