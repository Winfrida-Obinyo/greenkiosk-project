from django.contrib import admin

# Register your models here.


from .models import Discount
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent')
admin.site.register(Discount, DiscountAdmin)
