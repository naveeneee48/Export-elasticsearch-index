from os import EX_SOFTWARE
from elasticsearch import Elasticsearch, helpers
import sys, json

es = "http://10.3.18.237:9200/"

def getcount(index, url):
    try:
        es = Elasticsearch([url])
        doc = {
            "query": {"bool": {"must": [
                {"query_string": {
                    "query": "*"
                }}, {"range": {
                    "timestamp": {
                        "gte": "now-2y",
                        "lte": "now"
                    }
                }}
            ]}}
        }
        res = es.search(index=index, body=doc, request_timeout=30000)
        return res["hits"]["total"] 
    except: 
      print("index not found")

def getdoc(count, index,url):      
  try:
   es = Elasticsearch([url])
   doc = ({
  "size": count ,
  "query":
   {
    "match_all": {}
   }
   })
   res = es.search(index=index, body=doc, request_timeout=30000)
   write_json(res, index+".json")
  except:
    print("index not here")

def write_json(new_data, filename):
    with open(filename, 'w') as fp:
        json.dump(new_data, fp)
    print("Write successful")



def getConfig(filename):
    Config = {}
    with open(filename) as f:
        Config = json.load(f)
    return Config

config = {}
if len(sys.argv) != 2:
    print("Usage: python diskalert.py <config-name>")
    sys.exit(1)
config = getConfig(sys.argv[1:][0])

es = config["es_url"]

listofindexes = config["allindexes"]

for index in listofindexes:
  print (index)
  count = getcount (config["customer"]+"-"+index, es)
  getdoc (count , config["customer"]+"-"+index, es)

