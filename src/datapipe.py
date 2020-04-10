from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import scipy.stats as stats
from datetime import datetime

style.use('ggplot')

# instantiate start date and end date
start_date = '2017-01-01'
end_date = str(datetime.now().strftime('%Y-%m-%d'))

# import data from yahoo finance api using pandas_datareader

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

asset_list = [gold, dji, btc, ixic, eth, gspc, xrp]


def clean_data(asset_data, col, ticker):
    if '^' in ticker:
        weekdays = pd.date_range(start=start_date, end=end_date)
        clean_data = asset_data[col].reindex(weekdays)
        asset_data['Change'] = np.log(asset_data['Adj Close'] / asset_data['Adj Close'].shift())
        asset_data['Volatility 20'] = asset_data['Change'].rolling(20).std().shift()
        asset_data['Volatility 200'] = asset_data['Change'].rolling(200).std().shift()
        return clean_data.fillna(method='ffill')
    else:
        clean_data = asset_data[col]
        asset_data['Change'] = np.log(asset_data['Adj Close'] / asset_data['Adj Close'].shift())
        asset_data['Volatility 20'] = asset_data['Change'].rolling(20).std().shift()
        asset_data['Volatility 200'] = asset_data['Change'].rolling(20).std().shift()
        return clean_data.fillna(method='ffill')

    
def create_plot(asset_data, ticker):
    stats = get_stats(asset_data)
    plt.subplots(figsize=(15,8))
    plt.plot(asset_data, label=ticker)
    plt.plot(stats['short_rolling'], label='20 day moving average')
    plt.plot(stats['long_rolling'], label='200 day moving average')
    plt.xlabel('Year')
    plt.ylabel('Adj Closing Price')
    plt.legend(loc='upper left')
    plt.title('Asset Price Change Over Time')
    plt.show()


def volatility_plot(asset_data, ticker):
    fig, axs = plt.subplots(2, figsize=(8,4))
    fig.suptitle('Volatility Index 20 days(top) 200 days (bottom)')
    axs[0].plot(asset_data['Volatility 20'].iloc[-20:], label=ticker)
    axs[1].plot(asset_data['Volatility 200'].iloc[-200:], label=ticker)
    fig.tight_layout()
    fig.show()

    
    
    # future volume graph

    # ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    # ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
    # ax1.plot(asset_data, label=ticker)
    # ax1.plot(stats['short_rolling'], label='20 day moving average')
    # ax1.plot(stats['long_rolling'], label='200 day moving average')
    # ax2.bar(asset_data.index, asset_data['Volume'])
    
    
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
        adj_close = clean_data(asset_data, 'Adj Close', ticker)
        create_plot(adj_close, ticker)
        volatility_plot(asset_data, ticker)
        return asset_data

    
    except:
        print('No data found for {t}'.format(t=ticker))
        


dji_df = get_data(dji)

btc_df = get_data(btc)

ixic_df = get_data(ixic)

eth_df = get_data(eth)

gspc_df = get_data(gspc)

xrp_df = get_data(xrp)