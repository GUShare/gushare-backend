import pytest
from django.test import RequestFactory
from django.urls import reverse
from rest_framework.request import QueryDict, Request
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate

from api.models import Booking, Building, Room, User, Workplace

# This conftest file provides all necessary test data concerning project classes and auxiliary functions/classes.
# It will be imported by the conftest.py in the parent directory.


@pytest.fixture
def user_model_class():
    return User


@pytest.fixture
def building_model_class():
    return Building


@pytest.fixture
def room_model_class():
    return Room


@pytest.fixture
def workplace_model_class():
    return Workplace


@pytest.fixture
def booking_model_class():
    return Booking


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def plain_request_object(user_object):
    """
    This fixture provides a plain request object.
    :param user_object:
    :return:
    """
    request = APIRequestFactory().get(reverse("user-me"), data=QueryDict())
    force_authenticate(request, user=user_object)
    return Request(request)


def setup_view(view, request, *args, **kwargs):
    """
    Function to mimic a .as_view() call on a Class-Based-View for testing purposes.
    :param view:
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view
