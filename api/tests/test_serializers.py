import pytest

from api.serializers import BookingSerializer, BuildingSerializer


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
