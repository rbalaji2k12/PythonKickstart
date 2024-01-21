import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv(r'C:\Users\A719288\OneDrive - Atos\office-backup\rbala\personal\analysis\csv\cm16FEB2023bhav.csv')
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())