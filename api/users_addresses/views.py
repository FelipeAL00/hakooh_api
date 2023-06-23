from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAddress
from .serializers import UsersAddressSerializer

class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UsersAddressSerializer