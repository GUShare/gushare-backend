import pytest
from rest_framework.request import QueryDict

from api.models import Room, Workplace


@pytest.fixture
def valid_workplace_json(room_object):
    """
    This fixture provides a valid (according to the WorkplaceSerializer) JSON dictionary.
    :param room_object:
    :param room_object:
    :return: Dict
    """
    room = room_object.id
    in_room_id = 1
    equipment = ["1", "2", "5", "6"]
    maintenance_availebility = True
    maintenance_status = "This a text for the maintenance status"
    notification = "This is a note."

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
    :return: Workplace
    """
    return Workplace.objects.create(
        room=Room.objects.get(id=valid_workplace_json["room"]),
        in_room_id=valid_workplace_json["in_room_id"],
        equipment=valid_workplace_json["equipment"],
        maintenance_availebility=valid_workplace_json[
            "maintenance_availebility"
        ],
        maintenance_status=valid_workplace_json["maintenance_status"],
        notification=valid_workplace_json["notification"],
    )


@pytest.fixture
def workplace2_object(valid_workplace_json):
    """
    This fixture creates a workplace object.
    :return: Workplace
    """
    valid_workplace_json["in_room_id"] = 2
    return Workplace.objects.create(
        room=Room.objects.get(id=valid_workplace_json["room"]),
        in_room_id=valid_workplace_json["in_room_id"],
        equipment=valid_workplace_json["equipment"],
        maintenance_availebility=valid_workplace_json[
            "maintenance_availebility"
        ],
        maintenance_status=valid_workplace_json["maintenance_status"],
        notification=valid_workplace_json["notification"],
    )


@pytest.fixture
def workplace3_object(valid_workplace_json):
    """
    This fixture creates a workplace object.
    :return: Workplace
    """
    valid_workplace_json["in_room_id"] = 3
    return Workplace.objects.create(
        room=Room.objects.get(id=valid_workplace_json["room"]),
        in_room_id=valid_workplace_json["in_room_id"],
        equipment=valid_workplace_json["equipment"],
        maintenance_availebility=valid_workplace_json[
            "maintenance_availebility"
        ],
        maintenance_status=valid_workplace_json["maintenance_status"],
        notification=valid_workplace_json["notification"],
    )


@pytest.fixture
def room2_workplace1_object(valid_workplace_json, room2_object):
    valid_workplace_json["room"] = room2_object.id
    return Workplace.objects.create(
        room=Room.objects.get(id=valid_workplace_json["room"]),
        in_room_id=valid_workplace_json["in_room_id"],
        equipment=valid_workplace_json["equipment"],
        maintenance_availebility=valid_workplace_json[
            "maintenance_availebility"
        ],
        maintenance_status=valid_workplace_json["maintenance_status"],
        notification=valid_workplace_json["notification"],
    )
