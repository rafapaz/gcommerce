from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import IntegerField
from .models import Item, ItemCategory, ItemRating, ItemPhoto


class ItemCategorySerializer(ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'


class ItemRatingSerializer(ModelSerializer):
    class Meta:
        model = ItemRating
        fields = '__all__'


class ItemPhotoSerializer(ModelSerializer):
    class Meta:
        model = ItemPhoto
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    category = ItemCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
