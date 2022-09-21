from turtle import title
from django.db import models

class WatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=20)
    review = models.CharField(max_length=222)

