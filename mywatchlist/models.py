from django.db import models

class MyWatchList(models.Model):
    watched = models.TextField(default='')
    title = models.TextField(default='')
    rating = models.IntegerField() 
    release_date = models.DateField()
    review = models.TextField(default='')