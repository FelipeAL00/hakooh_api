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