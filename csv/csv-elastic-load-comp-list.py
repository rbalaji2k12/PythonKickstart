from elasticsearch import Elasticsearch, helpers
import csv

es = Elasticsearch('http://localhost:9200')

with open('data/nifty-list/nifty_all.csv') as f:
    reader = csv.DictReader(f)
    response = helpers.bulk(es, reader, index='niftyall')
    print(response)
