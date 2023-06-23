from rest_framework import  serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Address
        fields = ['id', 'address', 'postal_code', 'number', 'complement', 'country', 'city', 'state']