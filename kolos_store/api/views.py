from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from common.views import ReadOnlyMixin

from products.models import Item, QuantityItemColorSize
from products.serializers import ItemSerializer, PatchQuantitySerializer


class AllItemsView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        items = Item.objects.all()
        paginator = self.pagination_class()
        paginated_items = paginator.paginate_queryset(
            items, request, view=self)

        item_serializer = ItemSerializer(paginated_items, many=True)

        return paginator.get_paginated_response(item_serializer.data)


class CustomPagination(PageNumberPagination):
    page_size = 10


class CasualItemView(ModelViewSet):
    queryset = Item.objects.filter(global_category__name='Casual')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class ClassicItemView(ModelViewSet):
    queryset = Item.objects.filter(global_category__name='Classic')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class MaleClassicItemView(ModelViewSet):
    queryset = Item.objects.filter(
        gender__name='Male', global_category__name='Classic')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class FemaleClassicItemView(ModelViewSet):
    queryset = Item.objects.filter(
        gender__name='Female', global_category__name='Classic')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class MaleCasualItemView(ModelViewSet):
    queryset = Item.objects.filter(
        gender__name='Male', global_category__name='Casual')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class FemaleCasualItemView(ModelViewSet):
    queryset = Item.objects.filter(
        gender__name='Female', global_category__name='Casual')
    serializer_class = ItemSerializer
    pagination_class = CustomPagination


class PatchItemView(ModelViewSet):
    queryset = QuantityItemColorSize.objects.all()
    serializer_class = PatchQuantitySerializer
    permission_classes = (IsAuthenticated,)
