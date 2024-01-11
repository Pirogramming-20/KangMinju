from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=32)
    year = models.CharField(max_length=32)
    GENRE_CHOICES = (
    ("action", "액션"),
    ("comedy", "코미디"),
    ("drama", "드라마"),
    ("romance", "로맨스"),
    ("thriller", "스릴러"),
    ("horror", "호러"),
    ("sci-fi", "SF"),
    ("fantasy", "판타지"),
    ("animation", "애니메이션"),
    ("documentary", "다큐멘터리"),
    ("musical", "뮤지컬"),
    ("mystery", "미스터리"),
    )
    genre = models.CharField(max_length=32, choices = GENRE_CHOICES)
    rating = models.CharField(max_length=32)
    time = models.CharField(max_length=32)
    review = models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32)
    
