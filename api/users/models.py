from django.db import models
import uuid

class User(models.Model):
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
    birth = models.DateField(
        null=False,
        blank=False
    )
    user_key = models.IntegerField()
    validated_birth = models.BooleanField(
        null=False, 
        blank=False
    )
