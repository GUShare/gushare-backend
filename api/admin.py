from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#
# from api.models import User
#
#
# class UserAdmin(BaseUserAdmin):
#
#     list_display = (
#         "id",
#         "email",
#         "username",
#         "first_name",
#         "last_name",
#         "date_joined",
#         "modified_at",
#     )
#     fieldsets = BaseUserAdmin.fieldsets
#     fieldsets[1][1]["fields"] += ("language", "dsgvo_accepted", "onboarding_passed")
#     ordering = ("-date_joined",)
#     readonly_fields = ("date_joined",)
#
#
# admin.site.register(User, UserAdmin)
