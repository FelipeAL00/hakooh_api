from rest_framework import  serializers
from .models import ProductOrder
class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['id', 'product_id', 'order_id'] 