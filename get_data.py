import requests
import pandas as pd

#Gets the time series data from symbols, and dates
def get_time_series(symbols, key, dates):
    time_series = {}

    for symbol in symbols:
        # Credit to https://www.alphavantage.co/documentation/
        # Gets time series data from alphavantage
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&apikey={1}'.format(symbol, key)
        r = requests.get(url)
        data = r.json()
        
        dict = {}
        for date in dates:
            dict[date] = float(data['Time Series (Daily)'][date]['4. close'])
        time_series[symbol] = dict
    return time_series

def get_portfolio_value(quantities, dates):
    time_series = get_time_series(list(quantities.keys()), '9AYSCICNWDM0RPZS', dates)
    val = 0
    for symbol, quantity in quantities.items():
        val += (time_series[symbol][dates[-1]] - time_series[symbol][dates[0]]) * quantity
    return val

print(get_portfolio_value({'IBM' : 1}, ['2021-09-28', '2021-09-27']))