https://eodhistoricaldata.com/cp/settings
https://www.nseindia.com/report-detail/eq_security

https://www.nseindia.com/regulations/listing-compliance/nse-market-capitalisation-all-companies
https://www.nseindia.com/products-services/indices-nifty-total-market-index
https://www.nseindia.com/all-reports  -> Archives -> Select for download : Full Bhavcopy and Security Deliverable data



curl -XGET http://localhost:9200/nifty/_search?pretty=true&q=*:*
http://localhost:9200/nifty/_search?size=5000&pretty=true
curl -X GET "http://localhost:9200/nifty/_search?size=5000&pretty=true"

curl -XGET localhost:9200/nifty/_search?pretty=true -H "Content-Type: application/json" -d "{ \"query\" : { \"query_string\" : { \"query\" : \"SYMBOL:ITC\" }  } }"

curl -XDELETE "http://localhost:9200/nifty"


 

