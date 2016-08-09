import json
import urllib.request

# based url and required header
url = "http://115.28.59.215:9270/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# auth user and password
data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "Admin",
                "password": "41hcH7XAVu2vuP9F"
            },
            "id": 0
        }).encode(encoding='UTF8')
print(type(data))
# create request object
request = urllib.request.urlopen(url, data,{'Content-Type': 'application/json'})
for key in header:
    request.add_header(key, header[key])
# auth and get authid
try:
    result = urllib.request.urlopen(request)
except urllib.request.URLError as e:
    print("Auth Failed, Please Check Your Name AndPassword:", e)
else:
    response = json.loads(result.read())
    result.close()
    print("Auth Successful. The Auth ID Is:", response['result'])
# import urllib.request
# import simplejson
# import json
#
# a = {'jsonrpc': '2.0', 'method': 'user.authenticate', 'params': {'user': 'Admin', 'password': '41hcH7XAVu2vuP9F'}, 'id': 1}
# b = simplejson.dumps(a).encode()
# c = urllib.request.urlopen('http://115.28.59.215:9270/api_jsonrpc.php', b, {'Content-Type': 'application/json'})
# d = urllib.request.urlopen(c)
# d.read()
