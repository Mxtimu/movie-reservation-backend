from django.urls import path
from .views import MovieListCreateView, MovieDetailView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'), #the <int:pk> tells Django to expect an id number so that is why that is why that is used
]