from django.shortcuts import render
from rest_framework import viewsets
from .models import Card, Payment, Wallet
from .serializers import CardSerializer, PaymentSerializer, WalletSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset =  Wallet.objects.all()
    serializer_class = WalletSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
