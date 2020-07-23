import btalib
import pandas as pd
import requests
import json
import btalib
import config
import OHLC
from datetime import datetime
import alpaca_trade_api as tradeapi


def getDailyData(self):
    # make a request to get data from alpaca
    dayBarsUrl = '{}/day?symbols={}&limit=200'.format(config.BARS_URL, self.tickers)
    r = requests.get(dayBarsUrl, headers=config.HEADERS)
    # format data in JSON for bta-lib analysis
    data = r.json()
    # writing data to text files, in csv format for btalib to process 
    # databases will be used at a later date
    for symbol in data:
        filename = 'data/DayOHLC/{}.txt'.format(symbol)
        f = open(filename, 'w+')
        # writes the columns for open, high, low, close data to a text file specifically for that ticker
        f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
        # writes the actual data under the correct column for each stock
        for bar in data[symbol]:
            t = datetime.fromtimestamp(bar['t'])
            day = t.strftime('%Y-%m-%d')
            line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
            f.write(line)
    f.close()
    print('Fetched daily data from alpaca api.')
    # now all data is in text files and the next functioon will do technical analysis on the data gathered
    dayTechAnalysis(self.symbols)


def dayTechAnalysis(symbols):
    for symbol in symbols:
        df = pd.read_csv('data/DayOHLC/{}.txt'.format(symbol), parse_dates=True, index_col='Date')
        sma5d = btalib.sma(df, period=5)
        df['5 day sma'] = sma5d.df
        sma200d = btalib.sma(df, period=200)
        df['200 day sma'] = sma200d.df
        rsi = btalib.rsi(df)
        df['rsi'] = rsi.df
        macd = btalib.macd(df)
        df['macd'] = macd.df['macd']
        df['signal'] = macd.df['signal']
        df['histogram'] = macd.df['histogram']
        df.to_csv(path_or_buf='data/DayOHLC/{}.txt'.format(symbol)) #, index='Date'
    print('Finished generating sma, rsi, macd.')

