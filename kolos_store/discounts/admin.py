# discounts/admin.py
from django.contrib import admin
from .models import Discount, UserDiscount, ProductDiscount


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'percentage', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('code', 'description')
    filter_horizontal = ('applicable_categories', 'applicable_genders')


admin.site.register(Discount, DiscountAdmin)
admin.site.register(UserDiscount)
admin.site.register(ProductDiscount)
