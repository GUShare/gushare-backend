from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from api.models import Booking, Building, Room, User, Workplace


class UserSerializer(serializers.Serializer):
    """
    Serializer only needed for GDPR-Export of User data.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "language",
            "date_joined",
            "modified_at",
            "dsgvo_accepted",
            "onboarding_passed",
            "favorite_workplaces",
            "last_login",
            "is_superuser",
        ]
        ref_name = "user-gdpr-serializers"


class DjoserUserSerializer(serializers.Serializer):
    class Meta:
        ref_name = "djoser-custom-serializer"

        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "language",
            "date_joined",
            "modified_at",
            "dsgvo_accepted",
            "onboarding_passed",
            "favorite_workplaces",
            "last_login",
            "is_superuser",
        ]


class BuildingSerializer(serializers.Serializer):
    class Meta:
        model = Building
        fields = "__all__"


class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = "__all__"


class WorkplaceSerializer(serializers.Serializer):
    class Meta:
        model = Workplace
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def to_internal_value(self, data):
        request = self.context["request"]
        data["user"] = request.user.id

        return super().to_internal_value(data)

    def validate(self, data):
        user = data.get("user")
        started = data.get("started")
        stopped = data.get("stopped")
        workplaces = data.get("workplaces")
        uuid = None

        if self.instance and (
            self.partial or self.context["request"].method == "PUT"
        ):
            uuid = self.instance.id
            started = data.get("started", self.instance.started)
            stopped = data.get("stopped", self.instance.stopped)

        # validate that started and stopped are on the same day
        if not (started.date() == stopped.date()):
            raise serializers.ValidationError(
                _("A booking must start and end on the same day.")
            )

        # Validate Started is before stopped
        if started > stopped:
            raise serializers.ValidationError(
                _("The start of a booking must be set before its end.")
            )

        # Validate there is no other booking for those workplaces in this timeslot
        for workplace in workplaces:
            if Booking.objects.filter(
                started__lte=started,
                stopped__gt=started,
                workplaces__in=[workplace],
            ).exists():
                raise serializers.ValidationError(
                    _(
                        f"The started date is in the time of an already existing booking for the {workplace.in_room_id} in room {workplace.room.name} "
                    )
                )
            if Booking.objects.filter(
                started__lte=stopped,
                stopped__gt=stopped,
                workplaces__in=[workplace],
            ).exists():
                raise serializers.ValidationError(
                    _(
                        f"The stopped date is in the time of an already existing booking for the {workplace.in_room_id} in room {workplace.room.name} "
                    )
                )

        # Validate that if len(workplaces) > 1 all workplaces of this booking should be in one room
        if len(workplaces) > 1:
            base_room = Room.objects.filter(id=workplaces[0].room)
            for i in range(1, len(workplaces)):
                if workplaces[i].room != base_room.id:
                    raise serializers.ValidationError(
                        _(
                            "All Workplaces in a Room-Booking have to reference to the same Room."
                        )
                    )

        # Validate that a user have no other bookings in this time in the same Room-Type
        this_day_bookings = Booking.objects.filter(
            started__date=started.date(), user=user
        ).exclude(id=uuid)
        if len(this_day_bookings) > 0:
            this_booking_workplace_room = Room.objects.filter(
                id=Workplace.objects.filter(id=workplaces[0]).id
            )
            for booking in this_day_bookings:
                if (
                    Room.objects.filter(
                        id=Workplace.objects.filter(id=booking.workplaces[0]).id
                    ).type
                    != this_booking_workplace_room.type
                ):
                    if booking.started < started < booking.stopped:
                        raise serializers.ValidationError(
                            _(
                                "The started date is within an already existing booking of this user with equal room types."
                            )
                        )
                    if booking.started < stopped < booking.stopped:
                        raise serializers.ValidationError(
                            _(
                                "The stoped date is within an already existing booking of this user with equal room types."
                            )
                        )

        return data
