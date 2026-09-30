from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, OwnerProfile, TenantProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_active",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Informations supplémentaires",
            {
                "fields": (
                    "phone",
                    "role",
                )
            }
        ),
    )


@admin.register(OwnerProfile)
class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "verification_status",
        "national_id",
        "created_at",
        "updated_at",
    )

    list_filter = ("verification_status",)
    search_fields = ("user__username", "user__email")


@admin.register(TenantProfile)
class TenantProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "verification_status",
        "national_id",
        "created_at",
    )

    list_filter = ("verification_status",)
    search_fields = ("user__username", "user__email")