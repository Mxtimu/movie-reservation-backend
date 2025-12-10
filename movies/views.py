from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

# This view handles GET (List all) and POST (Create new)
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer