from django.shortcuts import render
from rest_framework import mixins, serializers, viewsets

from api.models import Booking, Building, Room, Workplace
from api.serializers import (
    BookingSerializer,
    BuildingSerializer,
    RoomSerializer,
    WorkplaceSerializer,
)


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    name = "buildings"


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    name = "rooms"


class WorkplaceViewSet(viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer

    name = "workplaces"


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    name = "bookings"
