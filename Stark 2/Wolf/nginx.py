#!/usr/bin/python
# conding:utf8

from optparse import OptionParser
import re
import pycurl
import StringIO
import sys
import urllib2
import subprocess
import threading
import os
from optparse import OptionParser

def parse_url(url):
    c = pycurl.Curl()
    b = StringIO.StringIO()
    c.setopt(c.URL, url)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(c.WRITEFUNCTION, b.write)
    c.perform()
    c.setopt(c.CONNECTTIMEOUT, 5)
    c.setopt(c.TIMEOUT, 5)
    status = c.getinfo(pycurl.HTTP_CODE)
    if status == 200:
        content = b.getvalue()
        return content
    c.close()
    b.close()

def nginx_download(version):
    nginx_package = "nginx-%s.tar.gz" % (version)
    url = "http://nginx.org/download/%s" % (nginx_package)
    if not os.path.exists("/root/%s" % (nginx_package)):
        print("download %s ..." % (nginx_package))
        f = urllib2.urlopen(url)
        data = f.read()
        with open("/root/%s" % (nginx_package), "wb") as nginx:
            nginx.write(data)
        print("download success")
    return 0
def list_nginx():
    url = "http://nginx.org/download/"
    content = parse_url(url)
    version = []
    p = re.compile(r'>(nginx-(.*?).tar.gz)<')
    for m in p.finditer(content):
        version.append(m.group(2))
    return version[:-21:-1]

def install_nginx(version):
    nginx_package = "nginx-%s.tar.gz" % (version)
    lua_module = "https://github.com/openresty/lua-nginx-module.git"
    echo_module = "https://github.com/openresty/echo-nginx-module.git"
    check_module = "https://github.com/yaoweibin/nginx_upstream_check_module"

    if not os.path.exists("/root/lua-nginx-module"):
        print("git lua-nginx-module ...")
        p = subprocess.call("git clone %s" % (lua_module), shell=True)
        if p == 0:
            print("git lua-nginx-module success")

    if not os.path.exists("/root/echo-nginx-module"):
        print("git echo-nginx-module ...")
        p = subprocess.call("git clone %s" % (echo_module), shell=True)
        if p == 0:
            print("git echo-nginx-module success")

    if not os.path.exists("/root/nginx_upstream_check_module"):
        print("git nginx_upstream_check_module ...")
        p = subprocess.call("git clone %s" % (check_module), shell=True)
        if p == 0:
            print("git nginx_upstream_check_module success")

    if not os.path.exists("/root/nginx-%s" % (version)):
        print("tar %s ..." % (nginx_package))
        subprocess.call("tar -xzvf %s" % (nginx_package), shell=True)
        print("tar success")

    print("install %s ..." % (nginx_package))
    p = subprocess.call("cd /root/nginx-%s;./configure --prefix=/usr/local/nginx-%s --with-http_ssl_module --with-http_gzip_static_module --with-http_ssl_module --with-http_spdy_module --with-http_stub_status_module --add-module=/root/lua-nginx-module --add-module=/root/echo-nginx-module --add-module=/root/nginx_upstream_check_module" % (version, version), shell=True)
    if p == 0:
        p = subprocess.call("cd /root/nginx-%s;make" % (version), shell=True)
        if p == 0:
            subprocess.call("cd /root/nginx-%s;make install" % (version), shell=True)
            print("install %s success" % (nginx_package))
def main():
    parser = OptionParser()
    parser.add_option("-l", "--list", action="store_true", dest="list")
    parser.add_option("-i", "--version", action="store", dest="version")
    (options, args) = parser.parse_args()
    if options.list:
        for version in list_nginx():
            print(version)
    elif options.version:
        if options.version in list_nginx():
            if nginx_download(options.version) == 0:
                install_nginx(options.version)

if __name__ == '__main__':
    main()