from django.contrib import admin

# Register your models here.

from.models import notify

class notifyAdmin(admin.ModelAdmin):
    list_display=("name","message","date")

admin.site.register(notify,notifyAdmin)

