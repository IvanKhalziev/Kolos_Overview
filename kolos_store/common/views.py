from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.db.models import Q
from django.db.models import Max, Min


class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ReadOnlyMixin:
    permission_classes = [ReadOnlyPermission]


class PriceStatsMixin:
    def calculate_price_stats(self, queryset):
        max_price = queryset.aggregate(Max('price'))['price__max']
        min_price = queryset.aggregate(Min('price'))['price__min']

        self.request.min_price = min_price
        self.request.max_price = max_price


class SortingFilterMixin:
    def items_filters(self, queryset):
        max_price = self.request.query_params.get('max_price')
        min_price = self.request.query_params.get('min_price')
        category = self.request.query_params.get('category')
        sizes = self.request.query_params.getlist('size')
        gender = self.request.query_params.get('gender')

        size_filter = Q()

        for size in sizes:
            size_filter |= Q(sizes__name=size)

        queryset = queryset.filter(size_filter).distinct()

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if category:
            queryset = queryset.filter(category__name=category)

        if gender == 'Male':
            queryset = queryset.filter(gender__name='Male')

        if gender == 'Female':
            queryset = queryset.filter(gender__name='Female')

        return queryset
