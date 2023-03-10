# Generated by Django 4.1.7 on 2023-02-16 20:10

import uuid

import django.contrib.auth.models
import django.contrib.postgres.fields
import django.db.models.deletion
import location_field.models.plain
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("username", models.CharField(blank=True, max_length=151)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "language",
                    models.CharField(
                        choices=[("de", "Deutsch"), ("en", "English")],
                        default="de",
                        max_length=2,
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("dsgvo_accepted", models.BooleanField(default=False)),
                ("onboarding_passed", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Building",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("alternate_name", models.CharField(max_length=128)),
                ("description", models.TextField(max_length=500)),
                ("photo", models.ImageField(upload_to="")),
                ("telephone", models.CharField(max_length=50)),
                ("opening_hours", models.TextField()),
                ("address", models.CharField(max_length=255)),
                (
                    "geo",
                    location_field.models.plain.PlainLocationField(
                        default=None, max_length=63
                    ),
                ),
                ("map", models.ImageField(upload_to="")),
                ("maximum_attendee_capacity", models.IntegerField()),
                (
                    "amenity_feature",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[("1", "lift"), ("2", "parking deck")], max_length=3
                        ),
                        size=None,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("alternate_name", models.CharField(max_length=128)),
                ("description", models.TextField(max_length=500)),
                ("photo", models.ImageField(upload_to="")),
                ("room_location", models.ImageField(upload_to="")),
                (
                    "room_type",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[("1", "CoWorking"), ("2", "Meeting")], max_length=3
                        ),
                        size=None,
                    ),
                ),
                ("maintenance_availebility", models.BooleanField(default=True)),
                ("maintenance_status", models.TextField(max_length=250)),
                (
                    "building",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rooms",
                        to="api.building",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Workplace",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("in_room_id", models.IntegerField()),
                (
                    "equipment",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("1", "Phone"),
                                ("2", "Dual Screen"),
                                ("3", "Fax"),
                                ("4", "USB-C Docking-station"),
                                ("5", "Electric adjustable desk"),
                                ("6", "Printer"),
                                ("7", "Telephone"),
                            ],
                            max_length=3,
                        ),
                        size=None,
                    ),
                ),
                ("maintenance_availebility", models.BooleanField(default=True)),
                ("maintenance_status", models.TextField(max_length=250)),
                ("notification", models.TextField(max_length=500)),
                (
                    "favorite_workplace",
                    models.ManyToManyField(to=settings.AUTH_USER_MODEL),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workplaces",
                        to="api.room",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("started", models.DateTimeField()),
                ("stopped", models.DateTimeField()),
                (
                    "email_others",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=250), size=None
                    ),
                ),
                ("confirmed_at", models.DateTimeField(blank=True, null=True)),
                ("note", models.TextField(max_length=500)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("workplaces", models.ManyToManyField(to="api.workplace")),
            ],
        ),
    ]
