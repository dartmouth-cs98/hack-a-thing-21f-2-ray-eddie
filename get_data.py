from datetime import time
import requests
import pandas as pd

#Gets the time series data from symbols, and dates
def get_time_series(symbols, key, dates):
    time_series = {}

    for symbol in symbols:
        # Credit to https://www.alphavantage.co/documentation/
        # Gets time series data from alphavantage
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&outputsize=full&apikey={1}'.format(symbol, key)
        r = requests.get(url)
        data = r.json()
        dict = {}
        for date in dates:
            try:
                dict[date] = float(data['Time Series (Daily)'][date]['4. close'])
            except KeyError:
                continue
        time_series[symbol] = dict
    return time_series

with open('config.txt') as f:
    api_key = f.readline()
def get_portfolio_value(quantities, dates):
    time_series = get_time_series(list(quantities.keys()), '9AYSCICNWDM0RPZS', dates)
    dict = {}
    for date in dates:
        val = 0
        for symbol, quantity in quantities.items():
            if date in time_series[symbol]:
                val += (time_series[symbol][date])*quantity
        dict[date] = val
    time_series['Portfolio'] = dict
    return time_series

# print(get_time_series(['IBM'], '9AYSCICNWDM0RPZS',['2021-09-28', '2021-09-27']))