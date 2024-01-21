import yfinance as yahooFinance
 
# Here We are getting Facebook financial information
# We need to pass FB as argument for that
GetFacebookInformation = yahooFinance.Ticker("FB")
 
# whole python dictionary is printed here
print(GetFacebookInformation.info)
