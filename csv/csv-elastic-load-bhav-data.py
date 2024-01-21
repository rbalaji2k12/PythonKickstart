from elasticsearch import Elasticsearch, helpers
import csv
import os

dir = "./data/bhav-data"
filelist = os.listdir(dir)
print(filelist)

es = Elasticsearch('http://localhost:9200')

for filename in filelist:
    file = os.path.join(dir, filename)
    with open(file) as f:
        reader = csv.DictReader(f)
        response = helpers.bulk(es, reader, index='nifty')
        print(response)
