from django.db import models


# Create your models here.
class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    osversion = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    disk = models.CharField(max_length=50)
    vendor_id = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    cpu_core = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    Manufacturer = models.CharField(max_length=50)
    sn = models.CharField(max_length=50)

    def __str__(self):
        return self.name
