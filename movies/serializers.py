from rest_framework import serializers
from .models import Movie, CinemaHall, Showtime, Seat, Reservation


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'hall', 'row_number', 'seat_number', 'is_vip']


class ShowtimeSerializer(serializers.ModelSerializer):
    # We use the StringRelatedField so the API returns "Hall A" instead of just ID "1",  This makes it easier for the frontend to display names properly or user friendly.. .
    hall_name = serializers.CharField(source='hall.name', read_only=True)
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Showtime
        fields = ['id', 'movie', 'movie_title', 'hall', 'hall_name', 'start_time', 'price']


class ReservationSerializer(serializers.ModelSerializer):
    # Important Read-only fields = Data the server generates, user doesn't send these...
    user = serializers.StringRelatedField(read_only=True)
    movie_title = serializers.CharField(source='showtime.movie.title', read_only=True)
    seat_info = serializers.CharField(source='seat.__str__', read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'showtime', 'movie_title', 'seat', 'seat_info', 'booking_date', 'is_active']


        read_only_fields = ['user', 'booking_date', 'is_active']