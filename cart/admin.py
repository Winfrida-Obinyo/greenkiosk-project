from django.contrib import admin

# Register your models here.

from .models import cart


class addAdmin(admin.ModelAdmin):
    list_display=("quantity","price","shipping_price","Payment_method")

admin.site.register(cart,addAdmin)
