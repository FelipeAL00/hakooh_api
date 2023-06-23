from rest_framework import serializers
from .models import Card, Payment, Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Wallet
        fields = ['id', 'balance', 'user_id']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment  
        fields = ['id', 'payment_type', 'status', 'wallet_id']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'number', 'validate', 'cvv', 'holders_name', 'document', 'wallet_id']