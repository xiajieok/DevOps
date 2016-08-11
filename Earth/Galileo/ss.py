#!/usr/bin/env python
from subprocess import Popen, PIPE
import urllib
import urllib.request
import pickle
import json
import re
def get_CpuInfo():
    p = Popen(['cat','/Users/jack/cpuinfo'],stdout=PIPE,stderr=PIPE)
    stdout, stderr = p.communicate()
    cpudata = str(stdout.strip())
    print(cpudata)
    cpu_dict = {}
    re_cpu_cores = re.compile(r'processor\s+:\s+([\d])')
    re_vendor_id = re.compile(r'vendor_id\s+:\s([\w]+)')
    re_model_name = re.compile(r'model name\s+:\s+(.*)')

    res_cpu_cores = re_cpu_cores.findall(cpudata)
    print(res_cpu_cores)
    print(res_cpu_cores[0])
    cpu_dict['Cpu_Cores'] = int(res_cpu_cores[0]) + 1
    res_vendor_id = re_vendor_id.findall(cpudata)
    cpu_dict['Vendor_Id'] = res_vendor_id[-1]
    res_model_name = re_model_name.findall(cpudata)
    cpu_dict['Model_Name'] = res_model_name[-1]
    return cpu_dict
get_CpuInfo()