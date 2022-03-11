from urllib import response
import urllib.request
import json

url = 'http://openapi.seoul.go.kr:8088/65635156676b64773639536d456278/json/TbPublicWifiInfo/1/500'
response = urllib.request.urlopen(url)
json_str = response.read().decode('utf-8')
data = json.loads(json_str)
print(json.dumps(data, indent=4, ensure_ascii=False))

