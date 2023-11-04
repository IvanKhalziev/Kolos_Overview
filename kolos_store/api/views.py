# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination

from common.views import ReadOnlyMixin, SortingFilterMixin

from products.models import Item, QuantityItemColorSize, Collection, Category
from products.serializers import ItemSerializer, PatchQuantitySerializer, CollectionSerializer, CategorySerializer


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'amount_items'
    max_page_size = 30


class AllItemsView(ReadOnlyMixin, SortingFilterMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.all()

    def get_queryset(self):
        items = Item.objects.all()
        items = self.items_filters(items)
        return items


class CasualItemView(SortingFilterMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(global_category__name='Casual')

    def get_queryset(self):
        items = Item.objects.filter(global_category__name='Casual')
        items = self.items_filters(items)
        return items


class ClassicItemView(SortingFilterMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(global_category__name='Classic')

    def get_queryset(self):
        items = Item.objects.filter(global_category__name='Classic')
        items = self.items_filters(items)
        return items


class MaleClassicItemView(SortingFilterMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(
        gender__name='Male', global_category__name='Classic')

    def get_queryset(self):
        items = Item.objects.filter(
            gender__name='Male', global_category__name='Classic')
        items = self.items_filters(items)
        return items


class FemaleClassicItemView(SortingFilterMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(
        gender__name='Female', global_category__name='Classic')

    def get_queryset(self):
        items = Item.objects.filter(
            gender__name='Female', global_category__name='Classic')
        items = self.items_filters(items)
        return items


class MaleCasualItemView(SortingFilterMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(
        gender__name='Male', global_category__name='Casual')

    def get_queryset(self):
        items = Item.objects.filter(
            gender__name='Male', global_category__name='Casual')
        items = self.items_filters(items)
        return items


class FemaleCasualItemView(SortingFilterMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(
        gender__name='Female', global_category__name='Casual')

    def get_queryset(self):
        items = Item.objects.filter(
            gender__name='Female', global_category__name='Casual')
        items = self.items_filters(items)
        return items


class PatchItemView(SortingFilterMixin, ModelViewSet):
    queryset = QuantityItemColorSize.objects.all()
    serializer_class = PatchQuantitySerializer
    permission_classes = (IsAuthenticated,)


class CollectionView(ReadOnlyMixin, ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CategoryView(ReadOnlyMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
