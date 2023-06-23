from django.db import models
import uuid

from addresses.models import Address
from payments.models import Payment

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
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
