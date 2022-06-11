from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    empty_value_display = '---'
    list_display = ('username', 'phone')
