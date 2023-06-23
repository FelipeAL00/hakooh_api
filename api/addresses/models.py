from django.db import models
import uuid

class Address(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True    
    )
    address = models.CharField(
        null=False,
        blank=False,
    )
    postal_code = models.IntegerField(
        null=False,
        blank=False,
    )
    number = models.IntegerField(
        null=False,
        blank=False,
    )
    complement = models.TextField()
    country = models.CharField(
        null=False,
        blank=False
    )
    city = models.CharField(
        null=False,
        blank=False
    )
    state = models.CharField(
        null=False,
        blank=False
    )