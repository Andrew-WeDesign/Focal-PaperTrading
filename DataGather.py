from datetime import datetime, timedelta
import time
import requests
import pandas as pd
import btalib
import json

import config

def getFftnMinData(self):
    fftnMinBarUrl = '{}/15Min?symbols={}&limit=120'.format(config.BARS_URL, self.tickers) 
    r = requests.get(fftnMinBarUrl, headers=config.HEADERS)
    data = r.json()
    for symbol in data:
        filename = 'data/15MinOHLC/{}.json'.format(symbol)
        f = open(filename, 'w+')
        f.write('{' + '"{}": '.format(symbol) + json.dumps(data[symbol], indent=4) + '}')
        f.close()
    for symbol in data:
        filename = 'data/15MinOHLC/{}.txt'.format(symbol)
        f = open(filename, 'w+')
        f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
        tNow = datetime.now()
        tDelta = timedelta(days=119)
        tStart = tNow - tDelta
        tdAdd = timedelta(days=1)
        tPresent = tStart
        for bar in data[symbol]:
            day = tPresent.strftime('%Y-%m-%d')
            line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
            f.write(line)
            tPresent = tPresent + tdAdd
        f.close()
    print('Fetched fifteen minute data from alpaca api')
    for symbol in config.symbols:
        df = pd.read_csv('data/15MinOHLC/{}.txt'.format(symbol), parse_dates=True, index_col='Date')
        rsi = btalib.rsi(df)
        df['rsi'] = rsi.df
        stochastic = btalib.stochastic(df)
        df['stoc k'] = stochastic.df['k']
        df['stoc d'] = stochastic.df['d']
        macd = btalib.macd(df)
        df['macd'] = macd.df['macd']
        df['signal'] = macd.df['signal']
        df['histogram'] = macd.df['histogram']
        df.to_csv(path_or_buf='data/15MinOHLC/{}.txt'.format(symbol), index ='Entry') #, index='Date'
    print('Finished generating rsi and stochastic oscillator.')
