from datetime import datetime, timedelta
import time
import requests
import pandas as pd
import btalib
import json
import alpaca_trade_api as tradeapi

import config

class test6():
    def __init__(self):
        self.alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')
        self.tickers = ','.join(config.symbols)


    def getOneMinData(self):
        OneMinBarUrl = '{}/1Min?symbols={}&limit=120'.format(config.BARS_URL, self.tickers)
        r = requests.get(OneMinBarUrl, headers=config.HEADERS)
        data = r.json()
        for symbol in data:
            filename = 'data/1MinOHLC/{}.json'.format(symbol)
            f = open(filename, 'w+')
            f.write('{' + '"{}": '.format(symbol) + json.dumps(data[symbol], indent=4) + '}')
            f.close()

            filename2 = 'data/1MinMACD/{}.txt'.format(symbol)
            g = open(filename2, 'w+')
            # writes the columns for open, high, low, close data to a text file specifically for that ticker
            g.write('Date,Open,High,Low,Close,Volume,OpenInterest,Entry\n')
            # writes the actual data under the correct column for each stock
            i = 1
            tNow = datetime.now()
            tDelta = timedelta(days=119)
            tStart = tNow - tDelta
            tdAdd = timedelta(days=1)
            tPresent = tStart
            for bar in data[symbol]:
                day = tPresent.strftime('%Y-%m-%d')
                line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
                g.write(line)
                #print(i)
                i = i+1
                tPresent = tPresent + tdAdd
            g.close()
        print('Fetched one minute data from alpaca api')

    def minuteTechAnalysis(self):
        for symbol in config.symbols:
            df = pd.read_csv('data/1MinMACD/{}.txt'.format(symbol), parse_dates=True, index_col='Date')
            sma5d = btalib.sma(df, period=5)
            df['5 day sma'] = sma5d.df
            sma200d = btalib.sma(df, period=120)
            df['200 day sma'] = sma200d.df
            rsi = btalib.rsi(df)
            df['rsi'] = rsi.df
            macd = btalib.macd(df)
            df['macd'] = macd.df['macd']
            df['signal'] = macd.df['signal']
            df['histogram'] = macd.df['histogram']
            df.to_csv(path_or_buf='data/1MinMACD/{}.txt'.format(symbol), index ='Entry') #, index='Date'
        print('Finished generating sma, rsi, macd.')

ls = test6()
ls.getOneMinData()
ls.minuteTechAnalysis()