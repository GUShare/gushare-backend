import uuid

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


class TestUserFields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id_field(self, user_model_class):
        assert hasattr(user_model_class, "id")

    def test_model_has_email_field(self, user_model_class):
        assert hasattr(user_model_class, "email")

    def test_model_has_first_name_field(self, user_model_class):
        assert hasattr(user_model_class, "first_name")

    def test_model_has_last_name_field(self, user_model_class):
        assert hasattr(user_model_class, "last_name")

    def test_model_has_language_field(self, user_model_class):
        assert hasattr(user_model_class, "language")

    def test_model_has_created_at_field(self, user_model_class):
        assert hasattr(user_model_class, "date_joined")

    def test_model_has_modified_at_field(self, user_model_class):
        assert hasattr(user_model_class, "modified_at")

    def test_model_has_dsgvo_accepted_field(self, user_model_class):
        assert hasattr(user_model_class, "dsgvo_accepted")

    def test_model_has_onboarding_passed_field(self, user_model_class):
        assert hasattr(user_model_class, "onboarding_passed")

    def test_field_type_id(self, user_model_class):
        assert isinstance(user_model_class._meta.get_field("id"), models.UUIDField)

    def test_field_type_email(self, user_model_class):
        assert isinstance(user_model_class._meta.get_field("email"), models.EmailField)

    def test_field_type_first_name(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("first_name"), models.CharField
        )

    def test_field_type_last_name(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("last_name"), models.CharField
        )

    def test_field_type_language(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("language"), models.CharField
        )

    def test_field_type_created_at(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("date_joined"), models.DateTimeField
        )

    def test_field_type_modified_at(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("modified_at"), models.DateTimeField
        )

    def test_field_type_dsgvo_accepted(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("dsgvo_accepted"), models.BooleanField
        )

    def test_field_type_onboarding_passed(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("onboarding_passed"), models.BooleanField
        )

    def test_field_conf_id(self, user_model_class):
        field = user_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable
