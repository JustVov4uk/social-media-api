from django.contrib import admin

from user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_of_birth",
        "location",
        "biography",
        "created_at",
        "updated_at",
        "is_private",
    )
