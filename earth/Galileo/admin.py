from django.contrib import admin
from  Galileo import models
# Register your models here.
class asset_system(admin.ModelAdmin):
    list_display = ('ip_info','serv_info','cpu_info','disk_info','mem_info','load_info','mark_info')
admin.site.register(models.asset_system)
