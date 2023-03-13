import pytest
from rest_framework.request import QueryDict

from api.models import Building


@pytest.fixture
def valid_building_json():
    """
    This fixture provides a valid (according to the ContractSerializer) JSON dictionary.
    :return: Dict
    """
    name = "Test Building"
    alternate_name = "TB"
    description = "This is a test Building"
    telephone = "1234567"
    opening_hours = "wochentags von 08:00 bis 16:00 Uhr"
    address = "Am Testweg 42"
    maximum_attendee_capacity = 42
    amenity_feature = ["1", "2"]

    data = {
        "name": name,
        "alternate_name": alternate_name,
        "description": description,
        "telephone": telephone,
        "opening_hours": opening_hours,
        "address": address,
        "maximum_attendee_capacity": maximum_attendee_capacity,
        "amenity_feature": amenity_feature,
    }

    return data


@pytest.fixture
def valid_building_querydict(valid_building_json):
    """
    This fixture creates a QueryDict out of the valid_building_json.
    :param valid_building_json:
    :return: QueryDict
    """
    qdict = QueryDict("", mutable=True)
    qdict.update(valid_building_json)
    return qdict


@pytest.fixture
def building_object(valid_building_json):
    """
    This fixture creates a building object.
    :return: Building
    """
    return Building.objects.create(**valid_building_json)
