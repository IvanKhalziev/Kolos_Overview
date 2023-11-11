from .models import QuantityItemColorSize, Item, Category, GlobalCategory, Gender, Size, Color, Collection
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name', queryset=Category.objects.all())
    global_category = serializers.SlugRelatedField(
        slug_field='name', queryset=GlobalCategory.objects.all())
    gender = serializers.SlugRelatedField(
        slug_field='name', queryset=Gender.objects.all())
    collection = serializers.SlugRelatedField(
        slug_field='name', queryset=Collection.objects.all())
    sizes_color_quantity = serializers.SerializerMethodField()

    max_price = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('max_price', 'min_price', 'name', 'id', 'price', 'gender', 'global_category', 'category', 'collection', 'description',
                  'sizes_color_quantity')

    def get_max_price(self, instance):
        return self.context.get('request').max_price

    def get_min_price(self, instance):
        return self.context.get('request').min_price

    def get_sizes_color_quantity(self, item):
        sizes_colors_quantity_photos = QuantityItemColorSize.objects.filter(
            item=item)
        sizes_colors_quantity_photo_data = []

        for sizes_colors_quantity_photo in sizes_colors_quantity_photos:
            photos = sizes_colors_quantity_photo.photo_url
            photo_urls = [
                getattr(photos, f'photo_url_{i}', None) for i in range(1, 7)]

            sizes_colors_quantity_photo_data.append({
                'id': sizes_colors_quantity_photo.id,
                'discount': sizes_colors_quantity_photo.discount,
                'size': sizes_colors_quantity_photo.size.name,
                'color': sizes_colors_quantity_photo.color.name,
                'hex': sizes_colors_quantity_photo.color.hex,
                'quantity': sizes_colors_quantity_photo.quantity.quantity,
                'photo_urls': photo_urls,
            })

        sizes_order = self.context['request'].query_params.getlist('size', [])

        sizes_colors_quantity_photo_data.sort(key=lambda x: sizes_order.index(
            x['size']) if x['size'] in sizes_order else len(sizes_order))

        return sizes_colors_quantity_photo_data


class CategorySerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'gender')

    def get_gender(self, gender):
        return [gender.name for gender in gender.gender.all()]


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('id', 'name', 'description', 'photo_url')


class CategoryCollectionSerializer(serializers.Serializer):
    def to_representation(self, instance):
        categories_data = Category.objects.all()
        collections_data = Collection.objects.all()

        category_serializer = CategorySerializer(categories_data, many=True)
        collection_serializer = CollectionSerializer(
            collections_data, many=True)

        return {
            'categories': category_serializer.data,
            'collections': collection_serializer.data
        }


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
