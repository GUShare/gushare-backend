from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    BookingViewSet,
    BuildingViewSet,
    GDPRExportView,
    RoomViewSet,
    WorkplaceViewSet,
)

app_name = "api"
router = DefaultRouter()
router.register(
    r"buildings", BuildingViewSet, basename="buildings"
)  # Read only
router.register(r"rooms", RoomViewSet, basename="rooms")  # Read only
router.register(
    r"workplaces", WorkplaceViewSet, basename="workplaces"
)  # Read only
router.register(r"bookings", BookingViewSet, basename="bookings")  # CRUD

check_booking = RoomViewSet.as_view({"get": "check_booking"})

urlpatterns = [
    path(
        "check-booking/<str:room_uuid>/<int:day>/<int:month>/<int:year>",
        check_booking,
        name="check_booking",
    ),
    path("gdpr/", GDPRExportView.as_view({"get": "retrieve"})),
    path("", include(router.urls)),
]
