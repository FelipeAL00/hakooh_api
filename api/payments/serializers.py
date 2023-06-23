from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment  
        fields = ['id', 'payment_type', 'status', 'wallet_id']