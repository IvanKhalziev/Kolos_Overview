from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ReadOnlyMixin:
    permission_classes = [ReadOnlyPermission]


class SortingFilterMixin:
    def items_filters(self, queryset):
        max_price = self.request.query_params.get('max_price')
        min_price = self.request.query_params.get('min_price')
        sort_param = self.request.query_params.get('sort')
        category_param = self.request.query_params.get('category')

        if sort_param == 'size_S':
            queryset = queryset.filter(sizes__name='S')
        elif sort_param == 'size_M':
            queryset = queryset.filter(sizes__name='M')
        elif sort_param == 'size_L':
            queryset = queryset.filter(sizes__name='L')
        elif sort_param == 'size_XL':
            queryset = queryset.filter(sizes__name='XL')

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if category_param:
            queryset = queryset.filter(category__name=category_param)

        return queryset
