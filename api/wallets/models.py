from django.db import models
import uuid

from users.models import User

class Wallet(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True   
    )
    balance = models.DecimalField(
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=2
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   
class Card(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True   
    )
    number = models.CharField(
        null=False,
        blank=False
    )
    validate = models.DateField(
        null=False,
        blank=False
    )
    cvv = models.IntegerField(
        null=False,
        blank=False   
    )
    holders_name = models.CharField(
        null=False,
        blank=False
    )
    document = models.CharField(
        null=False,
        blank=False
    )
    wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE) 
    
class Payment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True   
    )
    payment_type = models.CharField(
        null=False,
        blank=False
    )
    status = models.IntegerField(
        null=False,
        blank=False,
    )
    wallet_id = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )