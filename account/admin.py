from django.contrib import admin
from .models import Profile, Airline


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'airline']


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ['airline',]