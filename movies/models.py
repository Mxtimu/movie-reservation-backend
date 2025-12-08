from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration_minutes = models.IntegerField()
    poster_image = models.URLField(blank=True, null=True)  # URL to an image

    def __str__(self):
        return self.title

class CinemaHall(models.Model):
    name = models.CharField(max_length=50) # e.g., "Hall A", "IMAX Screen"
    total_seats = models.IntegerField()

    def __str__(self):
        return self.name

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name='showtimes')
    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # e.g., 150.00

    def __str__(self):
        return f"{self.movie.title} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"