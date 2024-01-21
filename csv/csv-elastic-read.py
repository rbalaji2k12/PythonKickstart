from elasticsearch import Elasticsearch
from search import *

es = Elasticsearch('http://localhost:9200')

res = es.search(index="niftyall", query={ 'match_all' : {} },size=10000) 
symbol_list = [source['_source']['SYMBOL'] for source in res['hits']['hits']]

date = "-Jul-"

for symbol in symbol_list:
  es_alpha(es, symbol, date)  