from rest_framework import serializers
from .models import UserAddress
class UsersAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'user_id', 'address_id']