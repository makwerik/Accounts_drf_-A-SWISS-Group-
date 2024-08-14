from django.contrib import admin
from .models import Users


# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'mail', 'phone_number')
    search_fields = ('first_name', 'middle_name', 'last_name', 'mail', 'phone_number')
