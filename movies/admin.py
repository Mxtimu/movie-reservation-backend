from django.contrib import admin
from .models import Movie, CinemaHall, Showtime

# This allows me to manage these tables on the dashboard
admin.site.register(Movie)
admin.site.register(CinemaHall)
admin.site.register(Showtime)