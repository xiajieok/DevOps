import urllib.request
import http.cookiejar


# head: dict of header
def makeMyOpener(head={
                      039;Connection&#039;: &#039;Keep-Alive&#039;,
                       039;Accept&#039;: &#039;text/html, application/xhtml+xml, */*&#039;,
                      &  # 039;Accept-Language&#039;: &#039;en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3&#039;,
                      &  # 039;User-Agent&#039;: &#039;Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko&#039;
    }

    ):
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
header = []
for key, value in head.items():
    elem = (key, value)
    header.append(elem)
opener.addheaders = header
return opener

oper = makeMyOpener()
uop = oper.open( &  # 039;http://www.baidu.com/&#039;, timeout = 1000)
      data = uop.read()
print(data.decode())
