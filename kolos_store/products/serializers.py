from .models import QuantityItemColorSize, Item, Category, GlobalCategory, Gender, Size, Color, Quantity
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name', queryset=Category.objects.all())
    global_category = serializers.SlugRelatedField(
        slug_field='name', queryset=GlobalCategory.objects.all())
    gender = serializers.SlugRelatedField(
        slug_field='name', queryset=Gender.objects.all())
    sizes_color_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('name', 'id', 'price', 'gender', 'global_category', 'category', 'description',
                  'sizes_color_quantity')

    def get_sizes_color_quantity(self, item):
        sizes_colors = QuantityItemColorSize.objects.filter(item=item)
        sizes_color_data = []

        for size_color in sizes_colors:
            sizes_color_data.append({
                'id': size_color.id,
                'size': size_color.size.name,
                'color': size_color.color.name,
                'hex': size_color.color.hex,
                'quantity': size_color.quantity.quantity,
                'photo_url': size_color.photo_url,
            })

        return sizes_color_data


class PatchQuantitySerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(
        slug_field='name', queryset=Size.objects.all())
    color = serializers.SlugRelatedField(
        slug_field='name', queryset=Color.objects.all())

    """ Quantity_name = Quantity_id | Dont need to patch quantity_name """
    # quantity = serializers.SlugRelatedField(
    #     slug_field='quantity', queryset=Quantity.objects.all())

    class Meta:
        model = QuantityItemColorSize
        fields = ('id', 'size', 'color', 'quantity')
