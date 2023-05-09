from django.contrib import admin
from .models import *

class AdminAppointment(admin.ModelAdmin):
    list_display = ('id','user', 'service', 'dayIn', 'dayOut', 'price')
    list_display_links = ('id', 'user', 'service')


admin.site.register(Booking, AdminAppointment)