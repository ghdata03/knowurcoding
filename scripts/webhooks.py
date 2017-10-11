import urllib
import urllib2

payload = {"sender":{"login":"ghdata03","id": 10701994,"type":"User"}}
payload_urlencode = urllib.urlencode(payload)
requrl = "https://leancloud.cn/1.1/engine/groups/web/productionImage?token=7YOLP2WrFpafldyHMzu5lBymOWfEobjNrzXsvbBM0eyLCQLh3smBcF8TbV9Xv6mO&gitTag=master"

req = urllib2.Request(url=requrl,data=payload_urlencode)

print req

res_data = urllib2.urlopen(req)
res = res_data.read()

print res


