from elasticsearch import Elasticsearch, helpers
import csv

es = Elasticsearch('http://localhost:9200')

with open('ind_nifty200Quality30_list.csv') as f:
    reader = csv.DictReader(f)
    response = helpers.bulk(es, reader, index='nifty200')
    print(response)
