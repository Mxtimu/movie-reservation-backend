from rest_framework import viewsets, permissions
from .models import Movie, CinemaHall, Showtime, Seat, Reservation
from .serializers import (
    MovieSerializer,
    CinemaHallSerializer,
    ShowtimeSerializer,
    SeatSerializer,
    ReservationSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# --- The Test View (Keep this for testing) ---
class TestProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            "message": "Access Granted! You have a valid token.",
            "user": request.user.username
        })

# --- The Real ViewSets ---

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ShowtimeViewSet(viewsets.ModelViewSet):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # User only sees their own reservations
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically attach the logged-in user
        serializer.save(user=self.request.user)