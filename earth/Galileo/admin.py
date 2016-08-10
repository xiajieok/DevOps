from django.contrib import admin
from  Galileo import models


# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = [
        'hostname',
        'ip',
        'osversion',
        'memory',
        'disk',
        'vendor_id',
        'model_name',
        'cpu_core',
        'product',
        'Manufacturer',
        'sn']


admin.site.register(models.Host, HostAdmin)
