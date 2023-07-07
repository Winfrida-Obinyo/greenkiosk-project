from django.db import models

# Create your models here.




class Shipping(models.Model):
    order_number = models.CharField(max_length=32)
    carrier = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    estimated_delivery = models.DateField()
    def __str__(self):
        return f"Shipping for Order {self.order_number}"