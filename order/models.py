from django.db import models
from payment.models import Pay


   # Define your payment fields here

class Order(models.Model):
    payment = models.OneToOneField(Pay, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=32)
    quantity = models.PositiveBigIntegerField()
    total = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
