from django.contrib import admin

from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "owner",
        "property_type",
        "city",
        "status",
        "created_at",
    )

    list_filter = (
        "property_type",
        "status",
        "city",
    )

    search_fields = (
        "title",
        "description",
        "address",
        "neighborhood",
        "city",
        "owner__username",
        "owner__email",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        PropertyImageInline,
    ]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):

    list_display = (
        "property",
        "caption",
        "image",
        "created_at",
    )

    search_fields = (
        "title",
        "caption",
    )