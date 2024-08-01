from django.contrib import admin
from .models import MenuItem, Booking

# Register your models here.

@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = (id, 'Title', 'Price', 'Inventory')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (id, 'Name', 'No_of_guests', 'BookingDate')