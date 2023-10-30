# products/admin.py
from django.contrib import admin
from .models import GlobalCategory, Category, Gender, Color, Size, Item, QuantityItemColorSize, Quantity


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'global_category', 'category', 'gender', 'price')
    list_filter = ('global_category', 'category', 'gender', 'colors', 'sizes')
    search_fields = ('name', 'category__name', 'gender__name')
    filter_horizontal = ('colors', 'sizes')


admin.site.register(GlobalCategory)
admin.site.register(Category)
admin.site.register(Gender)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Item, ItemAdmin)
admin.site.register(QuantityItemColorSize)
admin.site.register(Quantity)
