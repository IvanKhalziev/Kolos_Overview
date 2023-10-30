# orders/admin.py
from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name',
                    'city', 'post_office', 'created')
    list_filter = ('created',)
    search_fields = ('user__username', 'first_name', 'last_name')
    readonly_fields = ('basket_history',)


admin.site.register(Order, OrderAdmin)
