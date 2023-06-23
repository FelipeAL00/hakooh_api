from django.db import models
import uuid

from users.models import Address
from wallets.models import Payment

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    name = models.CharField(
        null=False,
        blank=False
    )    
    description = models.TextField(
        null=False,
        blank=False
    )
    value = models.DecimalField(
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=2
    )

class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True   
    )
    status = models.IntegerField(
        null=False,
        blank=False 
    )
    products = models.ManyToManyField(Product)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)