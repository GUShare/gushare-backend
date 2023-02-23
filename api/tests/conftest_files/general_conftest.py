import pytest

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
