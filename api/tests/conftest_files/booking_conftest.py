import datetime

import pytest
from django.conf import settings
from pytz import timezone
from rest_framework.request import QueryDict

from api.models import Booking, User, Workplace

tz = timezone(settings.TIME_ZONE)


@pytest.fixture
def valid_booking_json(workplace_object, user_object):
    """
    This fixture provides a valid (according to the BookingSerializer) JSON dictionary.
    :param workplace_object:
    :param user_object:
    :return: Dict
    """
    workplaces = [workplace_object.id]
    user = user_object.id
    started = datetime.datetime(2023, 1, 30, 14).astimezone(tz).isoformat()
    stopped = datetime.datetime(2023, 1, 30, 16).astimezone(tz).isoformat()
    email_others = ["testing1@test.de", "testing2@test.at"]
    confirmed_at = (
        datetime.datetime(2023, 1, 29, 14, 5).astimezone(tz).isoformat()
    )
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
    :return: Booking
    """
    return Booking.objects.create(
        user=User.objects.get(id=valid_booking_json["user"]),
        started=valid_booking_json["started"],
        stopped=valid_booking_json["stopped"],
        email_others=valid_booking_json["email_others"],
        confirmed_at=valid_booking_json["confirmed_at"],
        note=valid_booking_json["note"],
    ).workplaces.add(
        Workplace.objects.get(id=valid_booking_json["workplaces"][0])
    )


@pytest.fixture
def stopped_on_next_day_json(valid_booking_json):
    """
    This fixture creates an invalid according to the BookingSerializer
    where the stopped datetime is on the next day after the started datetime.
    :param valid_booking_json:
    :return: Dict
    """
    valid_booking_json["stopped"] = (
        datetime.datetime(2023, 1, 31, 16).astimezone(tz).isoformat()
    )
    return valid_booking_json


@pytest.fixture
def stopped_before_started_json(valid_booking_json):
    """
    This fixture creates an invalid according to the BookingSerializer
    where the stopped datetime is on the next day after the started datetime.
    :param valid_booking_json:
    :return: Dict
    """
    valid_booking_json["stopped"] = (
        datetime.datetime(2023, 1, 30, 12).astimezone(tz).isoformat()
    )
    return valid_booking_json
