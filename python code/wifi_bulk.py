from email.errors import HeaderParseError
import urllib.request
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers

es= Elasticsearch(
    cloud_id="SMUNavi:YXAtbm9ydGhlYXN0LTIuYXdzLmVsYXN0aWMtY2xvdWQuY29tOjkyNDMkMTJlMzFkMWI4ZGU1NGY2YWE4NDViYjAzOTI4MzhlZjkkNzIwMjRjZmZjNTJhNDJiZDkxODM3NmFlYThlYTQwMDU=",
    basic_auth=("elastic", "dCO4gIHI31E8giPJ7DOOm95C")
)

docs = []

for i in range(1, 21):
    iStart = (i-1)*1000 + 1
    iEnd = i*1000

    url = 'http://openapi.seoul.go.kr:8088/65635156676b64773639536d456278/xml/TbPublicWifiInfo/'+str(iStart)+'/'+str(iEnd)+'/'

    response = urllib.request.urlopen(url)
    xml_str = response.read().decode('utf-8')

    tree = ElementTree(fromstring(xml_str))
    root = tree.getroot()

    for row in root.iter("row"):
        gu_nm = row.find('X_SWIFI_WRDOFC').text
        place_nm = row.find('X_SWIFI_MAIN_NM').text
        place_x = float(row.find('LAT').text)
        place_y = float(row.find('LNT').text)
        doc = {
            "_index": "seoul_wifi",
            "_source": {
                "gu_nm": gu_nm,
                "place_nm": place_nm,
                "instl_xy": {
                    "lat": place_y,
                    "lon": place_x
                }
            }
        }
        docs.append(doc)
    print("END", iStart, "~", iEnd)
        
res = helpers.bulk(es, docs)
print("END")