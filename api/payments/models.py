from django.db import models
import uuid
from wallets.models import Wallet

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
