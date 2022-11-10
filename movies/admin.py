from django.contrib import admin
from movies.models import Movie, Watchlist

# Register your models here.
admin.site.register([Movie, Watchlist])