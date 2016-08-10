from django.shortcuts import render
from django.http import HttpResponse
from Galileo import models


# Create your views here.
def index(req):
    print(req)
    if req.method == 'POST':
        hostname = req.POST.get('hostname')
        ip = req.POST.get('ip')
        osversion = req.POST.get('osversion')
        memory = req.POST.get('memory')
        disk = req.POST.get('disk')
        vendor_id = req.POST.get('vendor_id')
        model_name = req.POST.get('model_name')
        cpu_core = req.POST.get('cpu_core')
        product = req.POST.get('product')
        Manufacturer = req.POST.get('Manufacturer')
        sn = req.POST.get('sn')
        try:
            host = models.Host.objects.get(hostname=hostname)
        except:
            host = models.Host()
        host.hostname = hostname
        host.ip = ip
        host.osversion = osversion
        host.memory = memory
        host.disk = disk
        host.vendor_id = vendor_id
        host.model_name = model_name
        host.cpu_core = cpu_core
        host.product = product
        host.Manufacturer = Manufacturer
        host.sn = sn
        host.save()

        return HttpResponse('ok')
    else:
        return HttpResponse('no data')
