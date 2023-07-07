from django.contrib import admin

# Register your models here.
from.models import Pay

class PayAdmin(admin.ModelAdmin):
    list_display= ("name","amount","Payment_method","status","date_created")

admin.site.register(Pay, PayAdmin)
