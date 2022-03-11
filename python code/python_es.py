from elasticsearch import Elasticsearch

es= Elasticsearch(
    cloud_id="SMUNavi:YXAtbm9ydGhlYXN0LTIuYXdzLmVsYXN0aWMtY2xvdWQuY29tOjkyNDMkMTJlMzFkMWI4ZGU1NGY2YWE4NDViYjAzOTI4MzhlZjkkNzIwMjRjZmZjNTJhNDJiZDkxODM3NmFlYThlYTQwMDU=",
    basic_auth=("elastic", "dCO4gIHI31E8giPJ7DOOm95C")
)

doc = {"name": "kim", "age": 35}
res = es.index(index='test_index', document=doc)
print(res)

doc = {
    "size" : 1,
    "query": {
        "term" : {
            "DestCityName" : "Seoul"
        }
    }
}

res = es.search(index='kibana_sample_data_flights', document=doc)
print(res)