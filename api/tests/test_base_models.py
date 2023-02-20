import pytest
from django.db import models


class TestUserModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object User can be imported.
        :return:
        """

        from api.models import User

    def test_model_is_model(self):
        """
        Test if the User Object is a Django Model
        :return:
        """
        from api.models import User

        assert issubclass(User, models.Model)


class TestBuildingModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object Building can be imported.
        :return:
        """

        from api.models import Building

    def test_model_is_model(self):
        """
        Test if the Building Object is a Django Model
        :return:
        """
        from api.models import Building

        assert issubclass(Building, models.Model)


class TestRoomModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object Room can be imported.
        :return:
        """

        from api.models import Room

    def test_model_is_model(self):
        """
        Test if the Room Object is a Django Model
        :return:
        """
        from api.models import Room

        assert issubclass(Room, models.Model)


class TestWorkplaceModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object Workplace can be imported.
        :return:
        """

        from api.models import Workplace

    def test_model_is_model(self):
        """
        Test if the Workplace Object is a Django Model
        :return:
        """
        from api.models import Workplace

        assert issubclass(Workplace, models.Model)


class TestBookingModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object Booking can be imported.
        :return:
        """

        from api.models import Booking

    def test_model_is_model(self):
        """
        Test if the Booking Object is a Django Model
        :return:
        """
        from api.models import Booking

        assert issubclass(Booking, models.Model)
