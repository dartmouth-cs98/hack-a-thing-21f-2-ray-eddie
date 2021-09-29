import requests
import pandas as pd

def get_time_series(symbols, key, dates):
    for symbol in symbols:
        # Credit to https://www.alphavantage.co/documentation/
        # Gets time series data from alphavantage
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&apikey={1}'.format(symbol, key)
        r = requests.get(url)
        data = r.json()
        
        dict = {}
        for date in dates:
            dict[date] = data['Time Series (Daily)'][date]['4. close']
        df = pd.Series(dict).to_frame()
        print(df)

get_time_series(['IBM'], '9AYSCICNWDM0RPZS', ['2021-09-28', '2021-09-27'])