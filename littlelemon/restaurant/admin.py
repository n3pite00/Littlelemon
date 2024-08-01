from django.contrib import admin
from .models import Menu, Booking

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (id, 'Name', 'No_of_guests', 'BookingDate')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (id, 'Title', 'Price', 'Inventory')