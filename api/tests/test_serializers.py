import pytest

from api.serializers import BookingSerializer, BuildingSerializer, WorkplaceSerializer, RoomSerializer


class TestBuildingSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the BookingSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(
        self, valid_building_querydict, plain_request_object
    ):
        """
        The BuildingSerializer is tested if a valid JSON passes validation.
        :param valid_building_querydict:
        :param plain_request_object:
        :return:
        """
        BuildingSerializer(
            data=valid_building_querydict, context={"request": plain_request_object}
        ).is_valid(raise_exception=True)


class TestRoomSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the RoomSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(self, valid_room_querydict, plain_request_object):
        """
        The RoomSerializer is tested if a valid JSON passes validation.
        :param valid_room_querydict:
        :param plain_request_object:
        :return:
        """
        RoomSerializer(
            data=valid_room_querydict, context={"request": plain_request_object}
        ).is_valid(raise_exception=True)


class TestWorkplaceSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the WorkplaceSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(
        self, valid_workplace_querydict, plain_request_object
    ):
        """
        The WorkplaceSerializer is tested if a valid JSON passes validation.
        :param valid_workplace_querydict:
        :param plain_request_object:
        :return:
        """
        WorkplaceSerializer(
            data=valid_workplace_querydict, context={"request": plain_request_object}
        ).is_valid(raise_exception=True)


class TestBookingSerializerValidation:
    """
    This Testsuite summarizes the Validation and Representation of the WorkplaceSerializer.
    """

    @pytest.mark.django_db
    def test_validate_correct_data(
        self, valid_booking_querydict, plain_request_object
    ):
        """
        The BookingSerializer is tested if a valid JSON passes validation.
        :param valid_workplace_querydict:
        :param plain_request_object:
        :return:
        """
        BookingSerializer(
            data=valid_booking_querydict, context={"request": plain_request_object}
        ).is_valid(raise_exception=True)
