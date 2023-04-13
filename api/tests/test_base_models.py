import uuid

import pytest
from django.contrib.postgres.fields import ArrayField
from django.db import models
from location_field.models.plain import PlainLocationField


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

    def test_model_has_favorite_workplaces_field(self, user_model_class):
        assert hasattr(user_model_class, "favorite_workplaces")

    def test_field_type_id(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("id"), models.UUIDField
        )

    def test_field_type_email(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("email"), models.EmailField
        )

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
            user_model_class._meta.get_field("date_joined"),
            models.DateTimeField,
        )

    def test_field_type_modified_at(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("modified_at"),
            models.DateTimeField,
        )

    def test_field_type_dsgvo_accepted(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("dsgvo_accepted"),
            models.BooleanField,
        )

    def test_field_type_onboarding_passed(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("onboarding_passed"),
            models.BooleanField,
        )

    def test_field_type_favorite_workplaces(self, user_model_class):
        assert isinstance(
            user_model_class._meta.get_field("favorite_workplaces"),
            models.ManyToManyField,
        )

    def test_field_conf_id(self, user_model_class):
        field = user_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable

    def test_field_conf_favorite_workplaces(
        self, user_model_class, workplace_model_class
    ):
        field = user_model_class._meta.get_field("favorite_workplaces")
        assert issubclass(field.remote_field.model, workplace_model_class)


class TestBuildingFields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id_field(self, building_model_class):
        assert hasattr(building_model_class, "id")

    def test_model_has_name_field(self, building_model_class):
        assert hasattr(building_model_class, "name")

    def test_model_has_alternate_name_field(self, building_model_class):
        assert hasattr(building_model_class, "alternate_name")

    def test_model_has_description_field(self, building_model_class):
        assert hasattr(building_model_class, "description")

    def test_model_has_photo_field(self, building_model_class):
        assert hasattr(building_model_class, "photo")

    def test_model_has_telephone_field(self, building_model_class):
        assert hasattr(building_model_class, "telephone")

    def test_model_has_opening_hours_field(self, building_model_class):
        assert hasattr(building_model_class, "opening_hours")

    def test_model_has_address_field(self, building_model_class):
        assert hasattr(building_model_class, "address")

    def test_model_has_geo_field(self, building_model_class):
        assert hasattr(building_model_class, "geo")

    def test_model_has_map_field(self, building_model_class):
        assert hasattr(building_model_class, "map")

    def test_model_has_maximum_attendee_capacity_field(
        self, building_model_class
    ):
        assert hasattr(building_model_class, "maximum_attendee_capacity")

    def test_model_has_amenity_features_field(self, building_model_class):
        assert hasattr(building_model_class, "amenity_features")

    def test_field_type_id(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("id"), models.UUIDField
        )

    def test_field_type_name(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("name"), models.CharField
        )

    def test_field_type_alternate_name(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("alternate_name"),
            models.CharField,
        )

    def test_field_type_description(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("description"),
            models.TextField,
        )

    def test_field_type_photo(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("photo"), models.ImageField
        )

    def test_field_type_telephone(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("telephone"), models.CharField
        )

    def test_field_type_opening_hours(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("opening_hours"),
            models.TextField,
        )

    def test_field_type_address(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("address"), models.CharField
        )

    def test_field_type_geo(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("geo"), PlainLocationField
        )

    def test_field_type_map(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("map"), models.ImageField
        )

    def test_field_type_maximum_attendee_capacity(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("maximum_attendee_capacity"),
            models.IntegerField,
        )

    def test_field_type_amenity_features(self, building_model_class):
        assert isinstance(
            building_model_class._meta.get_field("amenity_features"), ArrayField
        )

    def test_field_conf_id(self, building_model_class):
        field = building_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable


class TestRoomFields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id_field(self, room_model_class):
        assert hasattr(room_model_class, "id")

    def test_model_has_building_field(self, room_model_class):
        assert hasattr(room_model_class, "building")

    def test_model_has_name_field(self, room_model_class):
        assert hasattr(room_model_class, "name")

    def test_model_has_alternate_name_field(self, room_model_class):
        assert hasattr(room_model_class, "alternate_name")

    def test_model_has_description_field(self, room_model_class):
        assert hasattr(room_model_class, "description")

    def test_model_has_photo_field(self, room_model_class):
        assert hasattr(room_model_class, "photo")

    def test_model_has_room_location_field(self, room_model_class):
        assert hasattr(room_model_class, "room_location")

    def test_model_has_room_type_field(self, room_model_class):
        assert hasattr(room_model_class, "room_type")

    def test_model_has_maintenance_availebility_field(self, room_model_class):
        assert hasattr(room_model_class, "maintenance_availebility")

    def test_model_has_maintenance_status_field(self, room_model_class):
        assert hasattr(room_model_class, "maintenance_status")

    def test_field_type_id(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("id"), models.UUIDField
        )

    def test_field_type_name(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("name"), models.CharField
        )

    def test_field_type_building(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("building"), models.ForeignKey
        )

    def test_field_type_alternate_name(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("alternate_name"), models.CharField
        )

    def test_field_type_description(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("description"), models.TextField
        )

    def test_field_type_photo(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("photo"), models.ImageField
        )

    def test_field_type_room_location(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("room_location"), models.ImageField
        )

    def test_field_type_room_type(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("room_type"), ArrayField
        )

    def test_field_type_maintenance_availebility(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("maintenance_availebility"),
            models.BooleanField,
        )

    def test_field_type_maintenance_status(self, room_model_class):
        assert isinstance(
            room_model_class._meta.get_field("maintenance_status"),
            models.TextField,
        )

    def test_field_conf_id(self, room_model_class):
        field = room_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable

    def test_field_conf_building(self, room_model_class, building_model_class):
        field = room_model_class._meta.get_field("building")
        assert issubclass(field.remote_field.model, building_model_class)


class TestWorkplaceFields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id_field(self, workplace_model_class):
        assert hasattr(workplace_model_class, "id")

    def test_model_has_room_field(self, workplace_model_class):
        assert hasattr(workplace_model_class, "room")

    def test_model_has_in_room_id_field(self, workplace_model_class):
        assert hasattr(workplace_model_class, "in_room_id")

    def test_model_has_equipment_field(self, workplace_model_class):
        assert hasattr(workplace_model_class, "equipment")

    def test_model_has_maintenance_availebility_field(
        self, workplace_model_class
    ):
        assert hasattr(workplace_model_class, "maintenance_availebility")

    def test_model_has_maintenance_status_field(self, workplace_model_class):
        assert hasattr(workplace_model_class, "maintenance_status")

    def test_model_has_notification_field(self, workplace_model_class):
        assert hasattr(workplace_model_class, "notification")

    def test_field_type_id(self, workplace_model_class):
        assert isinstance(
            workplace_model_class._meta.get_field("id"), models.UUIDField
        )

    def test_field_type_room(self, workplace_model_class):
        assert isinstance(
            workplace_model_class._meta.get_field("room"), models.ForeignKey
        )

    def test_field_type_in_room_id(self, workplace_model_class):
        assert isinstance(
            workplace_model_class._meta.get_field("in_room_id"),
            models.IntegerField,
        )

    def test_field_type_equipment(self, workplace_model_class):
        assert isinstance(
            workplace_model_class._meta.get_field("equipment"), ArrayField
        )

    def test_field_type_maintenance_availebility(self, workplace_model_class):
        assert isinstance(
            workplace_model_class._meta.get_field("maintenance_availebility"),
            models.BooleanField,
        )

    def test_field_type_maintenance_status(self, workplace_model_class):
        assert isinstance(
            workplace_model_class._meta.get_field("maintenance_status"),
            models.TextField,
        )

    def test_field_type_notification(self, workplace_model_class):
        assert isinstance(
            workplace_model_class._meta.get_field("notification"),
            models.TextField,
        )

    def test_field_conf_id(self, workplace_model_class):
        field = workplace_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable

    def test_field_conf_room(self, workplace_model_class, room_model_class):
        field = workplace_model_class._meta.get_field("room")
        assert issubclass(field.remote_field.model, room_model_class)


class TestBookingFields:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_id_field(self, booking_model_class):
        assert hasattr(booking_model_class, "id")

    def test_model_has_workplaces(self, booking_model_class):
        assert hasattr(booking_model_class, "workplaces")

    def test_model_has_user(self, booking_model_class):
        assert hasattr(booking_model_class, "user")

    def test_model_has_started(self, booking_model_class):
        assert hasattr(booking_model_class, "started")

    def test_model_has_stopped(self, booking_model_class):
        assert hasattr(booking_model_class, "stopped")

    def test_model_has_email_others(self, booking_model_class):
        assert hasattr(booking_model_class, "email_others")

    def test_model_has_confirmed_at(self, booking_model_class):
        assert hasattr(booking_model_class, "confirmed_at")

    def test_model_has_note(self, booking_model_class):
        assert hasattr(booking_model_class, "note")

    def test_field_type_id(self, booking_model_class):
        assert isinstance(
            booking_model_class._meta.get_field("id"), models.UUIDField
        )

    def test_field_type_workplaces(self, booking_model_class):
        assert isinstance(
            booking_model_class._meta.get_field("workplaces"),
            models.ManyToManyField,
        )

    def test_field_type_user(self, booking_model_class):
        assert isinstance(
            booking_model_class._meta.get_field("user"), models.ForeignKey
        )

    def test_field_type_started(self, booking_model_class):
        assert isinstance(
            booking_model_class._meta.get_field("started"), models.DateTimeField
        )

    def test_field_type_stopped(self, booking_model_class):
        assert isinstance(
            booking_model_class._meta.get_field("stopped"), models.DateTimeField
        )

    def test_field_type_email_others(self, booking_model_class):
        assert isinstance(
            booking_model_class._meta.get_field("email_others"), ArrayField
        )

    def test_field_type_confirmed_at(self, booking_model_class):
        assert isinstance(
            booking_model_class._meta.get_field("confirmed_at"),
            models.DateTimeField,
        )

    def test_field_type_note(self, booking_model_class):
        assert isinstance(
            booking_model_class._meta.get_field("note"), models.TextField
        )

    def test_field_conf_id(self, booking_model_class):
        field = booking_model_class._meta.get_field("id")
        assert field.primary_key
        assert field.default == uuid.uuid4
        assert not field.editable

    def test_field_conf_workplace(
        self, booking_model_class, workplace_model_class
    ):
        field = booking_model_class._meta.get_field("workplaces")
        assert issubclass(field.remote_field.model, workplace_model_class)

    def test_field_conf_user(self, booking_model_class, user_model_class):
        field = booking_model_class._meta.get_field("user")
        assert issubclass(field.remote_field.model, user_model_class)
