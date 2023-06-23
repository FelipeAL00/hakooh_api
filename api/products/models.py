from django.db import models
import uuid
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
