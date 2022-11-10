from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Watchlist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        primary_key=True,
    )
    movie = models.ManyToManyField(
        Movie, related_name='watchlists'
    )
    is_watched = models.BooleanField(default=False)