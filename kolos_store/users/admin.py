# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number',
                    'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name',
         'last_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff',
         'is_active', 'groups', 'user_permissions')}),
    )


admin.site.register(User, CustomUserAdmin)
