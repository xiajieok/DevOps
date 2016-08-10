from django.db import models


# Create your models here.

class asset_system(models.Model):
    ip_info = models.CharField(max_length=50)
    serv_info = models.CharField(max_length=50)
    cpu_info = models.CharField(max_length=50)
    disk_info = models.CharField(max_length=50)
    mem_info = models.CharField(max_length=50)
    load_info = models.CharField(max_length=50)
    mark_info = models.CharField(default='beijing_idc', max_length=50, blank=True)

    def __str__(self):

        return self.name
