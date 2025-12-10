# I am going to write two types of tests... A model test
#which just checks if the database saves properly and an API test
#which just checks if the URL will return a status 200


from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie


class MovieModelTest(TestCase):
    def setUp(self):
        # Take note of this Timu, This runs before every test
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date="2024-01-01",
            duration_minutes=120
        )

    def test_movie_string_representation(self):

        self.assertEqual(str(self.movie), "Test Movie")

    def test_movie_creation(self):

        self.assertEqual(Movie.objects.count(), 1)



class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie_data = {
            "title": "API Movie",
            "description": "Created via API Test",
            "release_date": "2025-01-01",
            "duration_minutes": 90
        }
        self.url = reverse('movie-list-create') # Finds the URL for 'api/movies/'

    def test_get_movies(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):

        response = self.client.post(self.url, self.movie_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if it actually exists in DB now, in this current moment
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().title, "API Movie")