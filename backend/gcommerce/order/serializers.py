from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import IntegerField
from .models import Order, ItemOrder, Cart
from item.models import Item
from item.serializers import ItemSerializer
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer


class ItemOrderSerializer(ModelSerializer):
    item = ItemSerializer(many=False, read_only=True)

    class Meta:
        model = ItemOrder
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    items = ItemOrderSerializer(many=True, read_only=True)
    userprofile = UserProfileSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
