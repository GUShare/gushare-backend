import pytest
from rest_framework.request import QueryDict

from api.models import Workplace


@pytest.fixture
def valid_workplace_json(room_object):
    """
    This fixture provides a valid (according to the WorkplaceSerializer) JSON dictionary.
    :param room_object:
    :param room_object:
    :return: Dict
    """
    room = str(room_object.id)
    in_room_id = 1
    equipment = ["1", "2", "5", "6"]
    maintenance_availebility = True
    maintenance_status = "This workplace is available"
    notification = "Take care, you will have the door in your back."

    data = {
        "room": room,
        "in_room_id": in_room_id,
        "equipment": equipment,
        "maintenance_availebility": maintenance_availebility,
        "maintenance_status": maintenance_status,
        "notification": notification,
    }

    return data


@pytest.fixture
def valid_workplace_querydict(valid_workplace_json):
    """
    This fixture creates a QueryDict out of the valid_workplace_json.
    :param valid_workplace_json:
    :return: QueryDict
    """
    qdict = QueryDict("", mutable=True)
    qdict.update(valid_workplace_json)
    return qdict


@pytest.fixture
def workplace_object(valid_workplace_json):
    """
    This fixture creates a workplace object.
    :return: Building
    """
    return Workplace.objects.create(**valid_workplace_json)
