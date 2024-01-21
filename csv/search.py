from elasticsearch import Elasticsearch
import numpy as np
es = Elasticsearch('http://localhost:9200')

def es_alpha(es, symbol, date):
    query_body = {
    "query": {
      "bool": {
        "must": [{
          "match": {      
            "SYMBOL": symbol
          }
        },
        {
          "match": {      
            " DATE1": date
          }
        },
        {
          "match": {      
            " SERIES": " EQ"
          }
        }]
      }
    }
  }

    res = es.search(index="nifty", body=query_body, size=10000)
    
    price_list = [source['_source'][' AVG_PRICE'] for source in res['hits']['hits']]
    date_list = [source['_source'][' DATE1'] for source in res['hits']['hits']]
    #print(price_list)
    #print(date_list)


    
    
    # creating stock data
    price_diff_list = []
 
    for index in range(len(price_list)):
        # print(index, end=" : ")
        # print(stocks[index].date, end=" : ")
        # print(stocks[index].price)
        if index < (len(price_list)-1):
            price_diff_list.append(float(price_list[index+1]) - float(price_list[index]))

    # print(price_diff_list)
    # print(np.average(price_diff_list))
    # print(np.std(price_diff_list))
    if(len(price_diff_list) == 18):
      print(format(symbol), ",", format(res['hits']['total']['value']), ",", "{:.2f}".format( np.average(price_diff_list)/np.std(price_diff_list)) )


 