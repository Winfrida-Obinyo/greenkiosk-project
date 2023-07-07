from django.contrib import admin

# Register your models here.

from .models import Order

class ordersAdmin(admin.ModelAdmin):
    list_display= ("name","quantity","total","date_created")

admin.site.register(Order,ordersAdmin)

