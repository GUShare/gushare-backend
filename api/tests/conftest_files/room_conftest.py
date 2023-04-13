import pytest
from rest_framework.request import QueryDict

from api.models import Building, Room


@pytest.fixture
def valid_room_json(building_object):
    """
    This fixture provides a valid (according to the RoomSerializer) JSON dictionary.
    :param building_object:
    :param building_object:
    :return: Dict
    """
    name = "Test Room"
    alternate_name = "TR"
    description = "This is a test Room"
    room_type = ["1"]
    building = str(building_object.id)
    maintenance_availebility = True
    maintenance_status = "This room is available"

    data = {
        "name": name,
        "alternate_name": alternate_name,
        "description": description,
        "room_type": room_type,
        "building": building,
        "maintenance_availebility": maintenance_availebility,
        "maintenance_status": maintenance_status,
    }

    return data


@pytest.fixture
def valid_room_querydict(valid_room_json):
    """
    This fixture creates a QueryDict out of the valid_room_json.
    :param valid_room_json:
    :return: QueryDict
    """
    qdict = QueryDict("", mutable=True)
    qdict.update(valid_room_json)
    return qdict


@pytest.fixture
def room_object(valid_room_json):
    """
    This fixture creates a room object.
    :return: Room
    """
    return Room.objects.create(
        name=valid_room_json["name"],
        alternate_name=valid_room_json["alternate_name"],
        description=valid_room_json["description"],
        room_type=valid_room_json["room_type"],
        building=Building.objects.get(id=valid_room_json["building"]),
        maintenance_availebility=valid_room_json["maintenance_availebility"],
        maintenance_status=valid_room_json["maintenance_status"],
    )


@pytest.fixture
def valid_room2_json(building_object):
    """
    This fixture provides a valid (according to the RoomSerializer) JSON dictionary.
    :param building_object:
    :param building_object:
    :return: Dict
    """
    name = "Test Room 2"
    alternate_name = "TR2"
    description = "This is a second test Room"
    room_type = ["1"]
    building = building_object.id
    maintenance_availebility = True
    maintenance_status = "This room is available"

    data = {
        "name": name,
        "alternate_name": alternate_name,
        "description": description,
        "room_type": room_type,
        "building": building,
        "maintenance_availebility": maintenance_availebility,
        "maintenance_status": maintenance_status,
    }

    return data


@pytest.fixture
def room2_object(valid_room2_json):
    """
    This fixture creates a room object.
    :return: Room
    """
    return Room.objects.create(
        name=valid_room2_json["name"],
        alternate_name=valid_room2_json["alternate_name"],
        description=valid_room2_json["description"],
        room_type=valid_room2_json["room_type"],
        building=Building.objects.get(id=valid_room2_json["building"]),
        maintenance_availebility=valid_room2_json["maintenance_availebility"],
        maintenance_status=valid_room2_json["maintenance_status"],
    )
