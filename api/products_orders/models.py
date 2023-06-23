from django.db import models
import uuid

from products.models import Product
from orders.models import Order

class ProductOrder(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default= uuid.uuid4,
        null=False,
        blank=False
    )
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)