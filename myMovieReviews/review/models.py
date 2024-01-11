from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    year = models.IntegerField()
    genre = models.CharField(max_length=32)
    rating = models.FloatField()
    time = models.IntegerField()
    review = models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32)
    
