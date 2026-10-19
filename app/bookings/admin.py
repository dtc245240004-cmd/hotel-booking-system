from django.contrib import admin
from .models import Room, Customer, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'room_type',
        'price',
        'capacity',
        'status',
    )

    list_filter = (
        'room_type',
        'status',
    )

    search_fields = (
        'number',
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'created_at',
    )

    search_fields = (
        'full_name',
        'email',
        'phone',
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'room',
        'check_in',
        'check_out',
        'guests',
        'total_price',
        'status',
    )

    list_filter = (
        'status',
        'check_in',
        'check_out',
    )

    search_fields = (
        'customer__full_name',
        'room__number',
    )
