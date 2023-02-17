from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse
from django.utils.html import format_html

from api.models import User, Building, Room, Workplace, Booking


class UserAdmin(BaseUserAdmin):

    list_display = (
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "date_joined",
        "modified_at",
    )
    fieldsets = BaseUserAdmin.fieldsets
    fieldsets[1][1]["fields"] += ("language", "dsgvo_accepted", "onboarding_passed")
    ordering = ("-date_joined",)
    readonly_fields = ("date_joined",)


admin.site.register(User, UserAdmin)


class BuildingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "alternate_name",
        "description",
        "photo",
        "telephone",
        "opening_hours",
        "address",
        "map",
        "maximum_attendee_capacity",
        "amenity_feature",
    )
    list_per_page = 10
    ordering = ("name",)


admin.site.register(Building, BuildingAdmin)


class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "link_building",
        "name",
        "alternate_name",
        "description",
        "photo",
        "room_location",
        "room_type",
        "maintenance_availebility",
        "maintenance_status",
    )
    list_per_page = 10
    ordering = ("name",)

    def link_building(self, obj):
        building = obj.building
        url = reverse("admin:api_building_change", args=[building.pk])
        return format_html('<a href="{}">{}</a>', url, building.pk)

    link_building.short_description = "building"


admin.site.register(Room, RoomAdmin)


class WorkplaceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "link_room",
        "in_room_id",
        "equipment",
        "maintenance_availebility",
        "maintenance_status",
        "notification",
        "link_users"
    )
    list_per_page = 10
    ordering = ("room", "in_room_id")

    def link_room(self, obj):
        room = obj.room
        url = reverse("admin:api_room_change", args=[room.pk])
        return format_html('<a href="{}">{}</a>', url, room.pk)

    link_room.short_description = "room"

    def link_users(self, obj):
        users = obj.user
        url = reverse("admin:api_building_change", args=[users.pk])
        return format_html('<a href="{}">{}</a>', url, users.pk)

    link_users.short_description = "favored_by"


admin.site.register(Workplace, WorkplaceAdmin)


class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "link_workplaces",
        "started",
        "stopped",
        "email_others",
        "confirmed_at",
        "note",
    )
    list_per_page = 10
    ordering = ("-started", "-stopped", "-confirmed_at")

    def link_workplaces(self, obj):
        workplaces = obj.workplace
        url = reverse("admin:api_room_change", args=[workplaces.pk])
        return format_html('<a href="{}">{}</a>', url, workplaces.pk)

    link_workplaces.short_description = "workplaces"


admin.site.register(Booking, BookingAdmin)
