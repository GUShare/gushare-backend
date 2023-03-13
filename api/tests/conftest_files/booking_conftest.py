import datetime

import pytest
from django.conf import settings
from pytz import timezone
from rest_framework.request import QueryDict

from api.models import Booking

tz = timezone(settings.TIME_ZONE)


@pytest.fixture
def valid_booking_json(workplace_object, user_object):
    """
    This fixture provides a valid (according to the BookingSerializer) JSON dictionary.
    :param room_object:
    :param room_object:
    :return: Dict
    """
    workplaces = [str(workplace_object.id)]
    user = str(user_object.id)
    started = datetime.datetime(2023, 1, 29, 14).astimezone(tz).isoformat()
    stopped = datetime.datetime(2023, 1, 29, 16).astimezone(tz).isoformat()
    email_others = ["test1@test.de", "test2@test.at"]
    confirmed_at = datetime.datetime(2023, 1, 29, 14, 5).astimezone(tz).isoformat()
    note = "This is a note."

    data = {
        "workplaces": workplaces,
        "user": user,
        "started": started,
        "stopped": stopped,
        "email_others": email_others,
        "confirmed_at": confirmed_at,
        "note": note,
    }

    return data


@pytest.fixture
def valid_booking_querydict(valid_booking_json):
    """
    This fixture creates a QueryDict out of the valid_booking_json.
    :param valid_booking_json:
    :return: QueryDict
    """
    qdict = QueryDict("", mutable=True)
    qdict.update(valid_booking_json)
    return qdict


@pytest.fixture
def booking_object(valid_booking_json):
    """
    This fixture creates a workplace object.
    :return: Building
    """
    return Booking.objects.create(**valid_booking_json)
