import requests

def get_time_series(symbols, key):
    for symbol in symbols:
        # Credit to https://www.alphavantage.co/documentation/
        # Gets time series data from alphavantage
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&apikey={1}'.format(symbol, key)
        r = requests.get(url)
        data = r.json()

        print(data)

get_time_series(['IBM'], '9AYSCICNWDM0RPZS')