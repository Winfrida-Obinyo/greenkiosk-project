from django.contrib import admin




# Register your models here.

from .models import Shipping
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'carrier', 'tracking_number', 'status', 'estimated_delivery')
admin.site.register(Shipping, ShippingAdmin)