from django.contrib import admin
from .models import Capsule

#Register your models here.

@admin.register(Capsule)
class CapsuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'updated_at')
    list_filter = ('available', 'created_at', 'updated_at')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
