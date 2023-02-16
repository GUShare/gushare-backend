import uuid
from django.contrib.postgres.fields import ArrayField
from location_field.models.plain import PlainLocationField

from django.db import models


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
