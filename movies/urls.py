from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    MovieViewSet,
    CinemaHallViewSet,
    ShowtimeViewSet,
    SeatViewSet,
    ReservationViewSet,
    TestProtectedView
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'halls', CinemaHallViewSet)
router.register(r'showtimes', ShowtimeViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
    path('test-protected/', TestProtectedView.as_view(), name='test-protected'),
]