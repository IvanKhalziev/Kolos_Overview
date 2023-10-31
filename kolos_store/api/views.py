from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination

from common.views import ReadOnlyMixin

from products.models import Item, QuantityItemColorSize
from products.serializers import ItemSerializer, PatchQuantitySerializer


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'amount_items'
    max_page_size = 30

class AllItemsView(APIView):
    pagination_class = CustomPagination

    def get(self, request):
        items = Item.objects.all()
        paginator = self.pagination_class()
        paginated_items = paginator.paginate_queryset(
            items, request, view=self)

        item_serializer = ItemSerializer(paginated_items, many=True)

        return paginator.get_paginated_response(item_serializer.data)



class CasualItemView(ReadOnlyMixin, ModelViewSet):
    queryset = Item.objects.filter(global_category__name='Casual')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class ClassicItemView(ReadOnlyMixin, ModelViewSet):
    queryset = Item.objects.filter(global_category__name='Classic')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class MaleClassicItemView(ReadOnlyMixin, ModelViewSet):
    queryset = Item.objects.filter(
        gender__name='Male', global_category__name='Classic')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class FemaleClassicItemView(ReadOnlyMixin, ModelViewSet):
    queryset = Item.objects.filter(
        gender__name='Female', global_category__name='Classic')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class MaleCasualItemView(ReadOnlyMixin, ModelViewSet):
    queryset = Item.objects.filter(
        gender__name='Male', global_category__name='Casual')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class FemaleCasualItemView(ReadOnlyMixin, ModelViewSet):
    queryset = Item.objects.filter(
        gender__name='Female', global_category__name='Casual')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class PatchItemView(ModelViewSet):
    queryset = QuantityItemColorSize.objects.all()
    serializer_class = PatchQuantitySerializer
    permission_classes = (IsAuthenticated,)
