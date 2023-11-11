# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination

from common.views import ReadOnlyMixin, SortingFilterMixin, PriceStatsMixin

from products.models import Item, QuantityItemColorSize, Collection, Category
from products.serializers import ItemSerializer, PatchQuantitySerializer, CollectionSerializer, CategorySerializer, CategoryCollectionSerializer
from .utils import CategoryCollectionMerge

from rest_framework.views import APIView
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'amount_items'
    max_page_size = 30


class AllItemsView(ReadOnlyMixin, SortingFilterMixin, PriceStatsMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def get_queryset(self):
        items = Item.objects.all()
        self.calculate_price_stats(items)
        items = self.items_filters(items)
        return items


class CasualItemView(SortingFilterMixin, PriceStatsMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(global_category__name='Casual')

    def get_queryset(self):
        items = Item.objects.filter(global_category__name='Casual')
        self.calculate_price_stats(items)
        items = self.items_filters(items)
        return items


class ClassicItemView(SortingFilterMixin, PriceStatsMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(global_category__name='Classic')

    def get_queryset(self):
        items = Item.objects.filter(global_category__name='Classic')
        self.calculate_price_stats(items)
        items = self.items_filters(items)
        return items


class MaleClassicItemView(SortingFilterMixin, PriceStatsMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(
        gender__name='Male', global_category__name='Classic')

    def get_queryset(self):
        items = Item.objects.filter(
            gender__name='Male', global_category__name='Classic')
        self.calculate_price_stats(items)
        items = self.items_filters(items)
        return items


class FemaleClassicItemView(SortingFilterMixin, PriceStatsMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(
        gender__name='Female', global_category__name='Classic')

    def get_queryset(self):
        items = Item.objects.filter(
            gender__name='Female', global_category__name='Classic')
        self.calculate_price_stats(items)
        items = self.items_filters(items)
        return items


class MaleCasualItemView(SortingFilterMixin, PriceStatsMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(
        gender__name='Male', global_category__name='Casual')

    def get_queryset(self):
        items = Item.objects.filter(
            gender__name='Male', global_category__name='Casual')
        self.calculate_price_stats(items)
        items = self.items_filters(items)
        return items


class FemaleCasualItemView(SortingFilterMixin, PriceStatsMixin, ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = CustomPagination
    queryset = Item.objects.filter(
        gender__name='Female', global_category__name='Casual')

    def get_queryset(self):
        items = Item.objects.filter(
            gender__name='Female', global_category__name='Casual')
        self.calculate_price_stats(items)
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


class CategoryCollectionView(APIView):
    def get(self, request):
        collection_data = Collection.objects.first()
        category_data = Category.objects.all()

        category_collection_merge = CategoryCollectionMerge(
            collection_data, category_data)

        serializer = CategoryCollectionSerializer(
            category_collection_merge)

        category_collection_merge_data = serializer.data

        return Response(category_collection_merge_data)
