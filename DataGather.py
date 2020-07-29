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


# def startOfDay(self):
#     # check to see if the day to day data is up to date
#     dateNow = datetime.now()
#     dateT = dateNow.strftime('%Y-%m-%d')
#     g = open('Status/LastDayScan.txt', 'r')
#     lastScan = g.read()
#     g.close()
#     if(lastScan != dateT):
#         print('Daily data is out of date, updating data.')
#         getDailyData(self)
#         g = open('Status/LastDayScan.txt', 'w+')
#         g.write(dateT)
#         g.close()
#     else:
#         print('Daily data is up to date.')

# def getDailyData(self):
#     # make a request to get data from alpaca
#     dayBarsUrl = '{}/day?symbols={}&limit=200'.format(config.BARS_URL, self.tickers)
#     r = requests.get(dayBarsUrl, headers=config.HEADERS)
#     # format data in JSON for bta-lib analysis
#     data = r.json()
#     # writing data to text files, in csv format for btalib to process 
#     # databases will be used at a later date
#     for symbol in data:
#         filename = 'data/DayOHLC/{}.txt'.format(symbol)
#         f = open(filename, 'w+')
#         # writes the columns for open, high, low, close data to a text file specifically for that ticker
#         f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
#         # writes the actual data under the correct column for each stock
#         for bar in data[symbol]:
#             t = datetime.fromtimestamp(bar['t'])
#             day = t.strftime('%Y-%m-%d')
#             line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
#             f.write(line)
#     f.close()
#     print('Fetched daily data from alpaca api.')
#     # now all data is in text files and the next functioon will do technical analysis on the data gathered
#     dayTechAnalysis(self)

# def dayTechAnalysis(self):
#     for symbol in config.symbols:
#         df = pd.read_csv('data/DayOHLC/{}.txt'.format(symbol), parse_dates=True, index_col='Date')
#         sma5d = btalib.sma(df, period=5)
#         df['5 day sma'] = sma5d.df
#         sma200d = btalib.sma(df, period=200)
#         df['200 day sma'] = sma200d.df
#         rsi = btalib.rsi(df)
#         df['rsi'] = rsi.df
#         macd = btalib.macd(df)
#         df['macd'] = macd.df['macd']
#         df['signal'] = macd.df['signal']
#         df['histogram'] = macd.df['histogram']
#         df.to_csv(path_or_buf='data/DayOHLC/{}.txt'.format(symbol)) #, index='Date'
#     print('Finished generating sma, rsi, macd.')

# def getOneMinData(self):
#     OneMinBarUrl = '{}/1Min?symbols={}&limit=120'.format(config.BARS_URL, self.tickers)
#     r = requests.get(OneMinBarUrl, headers=config.HEADERS)
#     data = r.json()
#     for symbol in data:
#         filename = 'data/1MinOHLC/{}.json'.format(symbol)
#         f = open(filename, 'w+')
#         f.write('{' + '"{}": '.format(symbol) + json.dumps(data[symbol], indent=4) + '}')
#         f.close()
#     for symbol in data:
#         filename = 'data/1MinMACD/{}.txt'.format(symbol)
#         f = open(filename, 'w+')
#         # writes the columns for open, high, low, close data to a text file specifically for that ticker
#         f.write('Date,Open,High,Low,Close,Volume,OpenInterest,Entry\n')
#         # writes the actual data under the correct column for each stock
#         tNow = datetime.now()
#         tDelta = timedelta(days=119)
#         tStart = tNow - tDelta
#         tdAdd = timedelta(days=1)
#         tPresent = tStart
#         for bar in data[symbol]:
#             day = tPresent.strftime('%Y-%m-%d')
#             line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
#             f.write(line)
#             tPresent = tPresent + tdAdd
#         f.close()
#     print('Fetched one minute data from alpaca api')

# def minuteTechAnalysis(self):
#     for symbol in config.symbols:
#         df = pd.read_csv('data/1MinMACD/{}.txt'.format(symbol), parse_dates=True, index_col='Date')
#         sma5d = btalib.sma(df, period=5)
#         df['5 day sma'] = sma5d.df
#         sma200d = btalib.sma(df, period=120)
#         df['200 day sma'] = sma200d.df
#         rsi = btalib.rsi(df)
#         df['rsi'] = rsi.df
#         macd = btalib.macd(df)
#         df['macd'] = macd.df['macd']
#         df['signal'] = macd.df['signal']
#         df['histogram'] = macd.df['histogram']
#         df.to_csv(path_or_buf='data/1MinMACD/{}.txt'.format(symbol), index ='Entry') #, index='Date'
#     print('Finished generating sma, rsi, macd.')
