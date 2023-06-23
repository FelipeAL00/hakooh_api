from django.db import models
from wallets.models import Wallet
import uuid

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

