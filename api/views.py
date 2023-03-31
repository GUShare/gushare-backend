from datetime import datetime

from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, serializers, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from unidecode import unidecode

from api.models import Booking, Building, Room, User, Workplace
from api.serializers import (
    BookingSerializer,
    BuildingSerializer,
    RoomSerializer,
    UserSerializer,
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

    def check_booking(self, request, room=None, date=None, *args, **kwargs):
        """
        Custom endpoint which retrieves all bookings corresponding to the provided <room> and <date> url params.
        The bookings are anonymized and listed for every workplace of this <room> separately.
        :param request:
        :param room:
        :param date:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = self.get_queryset().filter(id=room, started__date=date)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class WorkplaceViewSet(viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer

    name = "workplaces"


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    name = "bookings"

    def get_queryset(self):
        """
        Customized method to only retrieve Objects owned by the User issueing the request.
        :return:
        """
        user = self.request.user
        queryset = super(BookingViewSet, self).get_queryset()
        return queryset.filter(user__id=user.id)


@swagger_auto_schema(content_type="text/json")
class GDPRExportView(viewsets.ViewSet):
    def retrieve(self, request, *args, **kwargs):
        """
        Endpoint to download all saved Data associated with the requesting User.

        The Response contains a JSON file as attachment!
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = request.user
        json_object = self.construct_json_object(user)
        rendered = self.render_json_object(json_object)
        response = HttpResponse(rendered, content_type="text/json")
        date = datetime.now().strftime("%d_%m_%Y")
        response[
            "Content-Disposition"
        ] = "attachment; filename={0}_{1}_gdpr-export_{2}.json".format(
            unidecode(user.first_name), unidecode(user.last_name), date
        )
        return response

    def construct_json_object(self, user):
        booking_data = BookingSerializer(
            Booking.objects.filter(user=user), many=True
        ).data
        user_data = UserSerializer(
            User.objects.filter(user=user), many=True
        ).data

        return {
            "user_data": user_data,
            "booking_data": booking_data,
        }

    def render_json_object(self, json_object):
        return JSONRenderer().render(
            json_object, accepted_media_type="application/json; indent=4"
        )
