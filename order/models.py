from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils.timezone import now
from django.db import models

from .import *


class Order(models.Model):
    created = models.DateTimeField(default=now, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="orders",
        on_delete=models.SET_NULL,
    )

    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.TextField()

    method_payment = models.CharField(max_length=200, default=MethodPayment.CASH,
                              choices=MethodPayment.CHOICES)
    order_status = models.CharField(max_length=200, default=OrderStatus.NEW,
                              choices=OrderStatus.CHOICES)


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order, related_name="lines", editable=False, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "categories.Product",
        related_name="order_lines",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    quantity = models.IntegerField(validators=[MinValueValidator(1)])