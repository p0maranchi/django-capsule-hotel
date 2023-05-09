from django.contrib import admin
from .models import *

class AdminBooking(admin.ModelAdmin):
    list_display = ('id','user', 'capsule', 'dayIn', 'dayOut', 'price')
    list_display_links = ('id', 'user', 'capsule')


admin.site.register(Booking, AdminBooking)