import datetime

import pytest
from django.conf import settings
from pytz import timezone
from rest_framework import exceptions, serializers

from api.models import Booking
from api.serializers import (
    BookingSerializer,
    BuildingSerializer,
    RoomSerializer,
    UserSerializer,
    WorkplaceSerializer,
)

tz = timezone(settings.TIME_ZONE)


class TestBuildingSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the BuildingSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(
        self, valid_building_json, plain_request_object
    ):
        """
        The BuildingSerializer is tested if a valid JSON passes validation.
        :param valid_building_json:
        :param plain_request_object:
        :return:
        """
        BuildingSerializer(
            data=valid_building_json,
            context={"request": plain_request_object},
        ).is_valid(raise_exception=True)


class TestRoomSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the RoomSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(self, valid_room_json, plain_request_object):
        """
        The RoomSerializer is tested if a valid JSON passes validation.
        :param valid_room_json:
        :param plain_request_object:
        :return:
        """
        RoomSerializer(
            data=valid_room_json, context={"request": plain_request_object}
        ).is_valid(raise_exception=True)


class TestWorkplaceSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the WorkplaceSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(
        self, valid_workplace_json, plain_request_object
    ):
        """
        The WorkplaceSerializer is tested if a valid JSON passes validation.
        :param valid_workplace_json:
        :param plain_request_object:
        :return:
        """
        WorkplaceSerializer(
            data=valid_workplace_json,
            context={"request": plain_request_object},
        ).is_valid(raise_exception=True)


class TestBookingSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the BookingSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(
        self, valid_booking_json, plain_request_object
    ):
        """
        The BookingSerializer is tested if a valid JSON passes validation.
        :param valid_booking_json:
        :param plain_request_object:
        :return:
        """
        BookingSerializer(
            data=valid_booking_json,
            context={"request": plain_request_object},
        ).is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_stopped_on_nex_day_validation(
        self, stopped_on_next_day_json, plain_request_object
    ):
        """
        The BookingSerializer is tested whether it raises a ValidationError
        if the shift ends on a different day.
        :return:
        """
        with pytest.raises(serializers.ValidationError):
            BookingSerializer(
                data=stopped_on_next_day_json,
                context={"request": plain_request_object},
            ).is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_stopped_before_started_validation(
        self, stopped_before_started_json, plain_request_object
    ):
        """
        The BookingSerializer is tested whether it raises a ValidationError
        if the started and ended datetimes are causally incorrect.
        :return:
        """
        with pytest.raises(serializers.ValidationError):
            BookingSerializer(
                data=stopped_before_started_json,
                context={"request": plain_request_object},
            ).is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_stopped_within_an_existing_booking(
        self, valid_booking_json, booking_object, plain_request_object
    ):
        """
        The BookingSerializer is tested whether it raises a ValidationError
        if stopped is within the timeslot of an existing booking.
        :return:
        """
        valid_booking_json["started"] = (
            datetime.datetime(2023, 1, 30, 13).astimezone(tz).isoformat()
        )
        valid_booking_json["stopped"] = (
            datetime.datetime(2023, 1, 30, 15).astimezone(tz).isoformat()
        )
        with pytest.raises(serializers.ValidationError):
            BookingSerializer(
                data=valid_booking_json,
                context={"request": plain_request_object},
            ).is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_started_within_an_existing_booking(
        self, valid_booking_json, booking_object, plain_request_object
    ):
        """
        The BookingSerializer is tested whether it raises a ValidationError
        if started is within the timeslot of an existing booking.
        :return:
        """
        valid_booking_json["started"] = (
            datetime.datetime(2023, 1, 30, 15).astimezone(tz).isoformat()
        )
        valid_booking_json["stopped"] = (
            datetime.datetime(2023, 1, 30, 17).astimezone(tz).isoformat()
        )
        with pytest.raises(serializers.ValidationError):
            BookingSerializer(
                data=valid_booking_json,
                context={"request": plain_request_object},
            ).is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_workplaces_by_different_rooms(
        self,
        workplaces_in_two_different_rooms_booking_json,
        plain_request_object,
    ):
        """
        The BookingSerializer is tested whether it raises a ValidationError
        if workplaces are not all in the same room.
        :return:
        """
        with pytest.raises(serializers.ValidationError):
            BookingSerializer(
                data=workplaces_in_two_different_rooms_booking_json,
                context={"request": plain_request_object},
            ).is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_not_all_workplaces_by_same_rooms(
        self,
        workplaces_not_all_in_room_booking_json,
        workplace3_object,
        plain_request_object,
    ):
        """
        The BookingSerializer is tested whether it raises a ValidationError
        if booking includes more than 1 workplace but not all workplaces of a room.
        :return:
        """
        with pytest.raises(serializers.ValidationError):
            BookingSerializer(
                data=workplaces_not_all_in_room_booking_json,
                context={"request": plain_request_object},
            ).is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_started_within_an_other_booking_of_user(
        self,
        booking_object,
        same_user_started_within_other_booking_json,
        plain_request_object,
    ):
        """
        The BookingSerializer is tested whether it raises a ValidationError
        if started is within a booking of the same user.
        :return:
        """
        with pytest.raises(serializers.ValidationError):
            BookingSerializer(
                data=same_user_started_within_other_booking_json,
                context={"request": plain_request_object},
            ).is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_stopped_within_an_other_booking_of_user(
        self,
        booking_object,
        same_user_stopped_within_other_booking_json,
        plain_request_object,
    ):
        """
        The BookingSerializer is tested whether it raises a ValidationError
        if stopped is within a booking of the same user.
        :return:
        """
        with pytest.raises(serializers.ValidationError):
            BookingSerializer(
                data=same_user_stopped_within_other_booking_json,
                context={"request": plain_request_object},
            ).is_valid(raise_exception=True)


class TestUserSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the UserSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(self, valid_user_json, plain_request_object):
        """
        The USerSerializer is tested if a valid JSON passes validation.
        :param valid_user_json:
        :param plain_request_object:
        :return:
        """
        UserSerializer(
            data=valid_user_json,
            context={"request": plain_request_object},
        ).is_valid(raise_exception=True)
