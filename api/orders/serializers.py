from rest_framework import  serializers
from .models import Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'address_id', 'payment_id'] 