from django.shortcuts import render
from rest_framework import viewsets
from .models import Address, User
from .serializers import AddressSerializer, UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer