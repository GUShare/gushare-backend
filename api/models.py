import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from location_field.models.plain import PlainLocationField

from django.db import models


class User(AbstractUser):

    LANGUAGE_CHOICES = (("de", "Deutsch"), ("en", "English"))
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    username = models.CharField(max_length=151, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)  # Firstname is required
    last_name = models.CharField(max_length=100)  # Lastname is required
    language = models.CharField(choices=LANGUAGE_CHOICES, default="de", max_length=2)
    date_joined = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    dsgvo_accepted = models.BooleanField(default=False)
    onboarding_passed = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]


class Building(models.Model):
    AMENITY_CHOICES = (
        ("1", "lift"),
        ("2", "parking deck")
    )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=128)
    alternate_name = models.CharField(max_length=128)
    description = models.TextField(max_length=500)
    photo = models.ImageField()
    telephone = models.CharField(max_length=50)
    opening_hours = models.TextField()
    address = models.CharField(max_length=255)
    geo = PlainLocationField(based_fields=['city'], default=None)
    map = models.ImageField()
    maximum_attendee_capacity = models.IntegerField()
    amenity_feature = ArrayField(base_field=models.CharField(choices=AMENITY_CHOICES, max_length=3))


class Room(models.Model):
    ROOMTYPE_CHOICES = (
        ("1", "CoWorking"),
        ("2", "Meeting")
    )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    building = models.ForeignKey(to=Building, related_name="rooms", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    alternate_name = models.CharField(max_length=128)
    description = models.TextField(max_length=500)
    photo = models.ImageField()
    room_location = models.ImageField()
    room_type = ArrayField(base_field=models.CharField(choices=ROOMTYPE_CHOICES, max_length=3))
    maintenance_availebility = models.BooleanField(default=True)
    maintenance_status = models.TextField(max_length=250)
    # todo: permissions


class Workplace(models.Model):
    EQUIPMENT_CHOICES = (
        ("1", "Phone"),
        ("2", "Dual Screen"),
        ("3", "Fax"),
        ("4", "USB-C Docking-station"),
        ("5", "Electric adjustable desk"),
        ("6", "Printer"),
        ("7", "Telephone")
    )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    room = models.ForeignKey(to=Room, related_name="workplaces", on_delete=models.CASCADE)
    favorite_workplace = models.ManyToManyField(to=User)
    in_room_id = models.IntegerField()
    equipment = ArrayField(base_field=models.CharField(choices=EQUIPMENT_CHOICES, max_length=3))
    maintenance_availebility = models.BooleanField(default=True)
    maintenance_status = models.TextField(max_length=250)
    notification = models.TextField(max_length=500)


class Booking(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    workplace = models.ManyToManyField(to=Workplace)
    # users
    started = models.DateTimeField()
    stopped = models.DateTimeField()
    email_others = ArrayField(base_field=models.CharField(max_length=250))
    confirmed_at = models.DateTimeField(null=True, blank=True)
    note = models.TextField(max_length=500)
