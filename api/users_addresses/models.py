from django.db import models
import uuid

from users.models import User
from addresses.models import Address

class UserAddress(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True  
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)    
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)