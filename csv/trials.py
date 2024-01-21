for num, doc in enumerate(res['hits']['hits']):
    print ("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")
    # Use 'iteritems()` instead of 'items()' if using Python 2
    for key, value in doc.items():
        print (key, "-->", value)
    print ("\n\n")

res_comp = es.search(index="nifty", query={"match": {"SYMBOL":symbol}},size=10000) 
print("Got %d Hits:" % res_comp['hits']['total']['value'])

#res = es.search(index="nifty", query={ 'match_all' : {} },size=10000) 
    
# query_body = {
#   "query": {
#     "bool": {
#       "must": {
#         "match": {      
#           "SYMBOL": symbol
#         }
#       }
#     }
#   }
# }

# res = es.search(index="nifty", body=query_body, size=10000)


   class stock:
        def __init__(self, symbol, alpha):
            self.symbol = symbol
            self.alpha = alpha
    
        def print(self):
            print(self.symbol)
            print(self.alpha)

  stocks = []
  stocks.append(stock(date_list[index], price_list[index]))