from nse_daily import NSEDaily

nd = NSEDaily()
res= nd.download_by_date('20200904')
res2 = nd.download_by_date_range(date_start='20200907',date_end='20200915',num_workers=3)