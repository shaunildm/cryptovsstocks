from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


# instantiate start date and end date
start_date = '2005-01-01'
end_date = str(datetime.now().strftime('%Y-%m-%d'))

# import data from yahoo finance api using asset ticker

# Gold
gold = 'GC=F'
# Dow Jones Index
dji = '^DJI'
# S&P 500
gspc = '^GSPC'
# NASDAQ
ixic = '^IXIC'
# Bitcoin
btc = 'BTC-USD'
# Etherium
eth = 'ETH-USD'
# XRP/Ripple
xrp = 'XRP-USD'
# AIG
aig = 'AIG'
# Facebook
fb = 'FB'
# Amazon
amzn = 'AMZN'
# Apple
aapl = 'AAPL'
# Netflix
nflx = 'nflx'
# Google class-C
goog = 'goog'
# Google class-A
googl = 'googl'


# will use front fill method to replace missing values
def clean_data(asset_data, col):
    weekdays = pd.date_range(start=start_date, end=end_date)
    clean_data = asset_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')


def create_plot(asset_data, ticker):
    stats = get_stats(asset_data)
    plt.subplots(figsize=(12,8))
    plt.plot(asset_data, label=ticker)
    plt.plot(stats['short_rolling'], label='20 day moving average')
    plt.plot(stats['long_rolling'], label='200 day moving average')
    plt.xlabel('Date')
    pass


def get_stats(asset_data):
    return {
        'last': np.mean(asset_data.tail(1)),
        'short_mean': np.mean(asset_data.tail(20)),
        'long_mean': np.mean(asset_data.tail(200)),
        'short_rolling': asset_data.rolling(window=20).mean(),
        'long_rolling': asset_data.rolling(window=200).mean()
    }


def get_data(ticker):
    try:
        asset_data = data.DataReader(ticker,
                                     'yahoo',
                                     start_date,
                                     end_date
                                    )
        print(clean_data(asset_data, 'Adj Close'))
    
    except:
        print('No data found for {t}'.format(t=ticker))
        


# We will test with gold first
get_data(gold)