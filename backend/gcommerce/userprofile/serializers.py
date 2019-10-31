from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import IntegerField
from .models import Address, UserProfile


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    address = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'