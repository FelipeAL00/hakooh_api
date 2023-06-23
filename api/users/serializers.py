from rest_framework import serializers
from .models import Address, User

class AddressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Address
        fields = ['id', 'address', 'postal_code', 'number', 'complement', 'country', 'city', 'state', 'user_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'birth', 'user_key', 'validated_birth']
        

        