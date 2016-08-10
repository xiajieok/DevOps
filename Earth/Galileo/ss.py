#!/usr/bin/env python
# site www.tshare365.com
from subprocess import Popen, PIPE
import urllib
import urllib.request
import pickle
import json
import re


def get_HostnameInfo(file):
    with open(file, 'r') as fd:
        data = fd.read().split('\n')
        for line in data:
            if line.startswith('HOSTNAME'):
                hostname = line.split('=')[1]
                break
    return hostname


#####[Demi message]#####
def get_dmidecode():
    P = Popen(['dmidecode'], stdout=PIPE)
    data = P.stdout.read()
    lines = data.split('\n\n')
    dmidecode_line = lines[2]
    line = [i.strip() for i in dmidecode_line.split('\n') if i]
    Manufacturer = line[2].split(': ')[-1]
    product = line[3].split(': ')[-1]
    sn = line[5].split(': ')[-1]
    return Manufacturer, product, sn


if __name__ == '__main__':
    #####[get data]#####
    hostname = get_HostnameInfo('/etc/sysconfig/network')
    # Manufacturer,product,sn = get_dmidecode()

    #####[get dict]#####
    hostinfo = {
        'hostname': hostname,
        # 'ip':ip,
        # 'osversion':osversion,
        # 'memory':memory,
        # 'disk':disk,
        # 'vendor_id':Vendor_Id,
        # 'model_name':Model_Name,
        # 'cpu_core':Cpu_Cores,
        # 'product':product,
        # 'Manufacturer':Manufacturer,
        # 'sn':sn,
    }

    # data = urllib.parse.urlencode(hostinfo)
    data = urllib.parse.urlencode(hostinfo).encode(encoding='UTF8')
    req = urllib.request.urlopen('http://192.168.40.11/hostinfo', data)
