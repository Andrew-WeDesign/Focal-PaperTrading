import btalib
import pandas as pd
import config
import requests
import json
from datetime import datetime, timedelta

#symbols = ['AAPL', 'DOMO']
symbols = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA', 'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', 'OKTA', 'TWTR', 'TM', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM']
# symbols = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA',
#         'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW',
#         'OKTA', 'TWTR', 'TM', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM', 'FANG', 
#         'MXIM', 'JKHY', 'KEYS', 'FTNT', 'ROL', 'ANET', 'CPRT', 'FLT', 'HFC', 'BR', 
#         'TWTR', 'EVRG', 'ABMD', 'MSCI', 'TTWO', 'SIVB', 'IPGP', 'HII', 'NCLH', 'CDNS', 
#         'SBAC', 'IQV', 'MGM', 'RMD', 'AOS', 'PKG', 'DRE', 'BKR', 'HLT', 'RE']
# tickers is needed to trim [] & ''
tickers = ','.join(symbols)

##########################################################

# df = pd.read_csv('data/ohlc/AAPL.txt', parse_dates=True, index_col='Date')
# sma5d = btalib.sma(df, period=5)
# df['5 day sma'] = sma5d.df
# sma200d = btalib.sma(df, period=200)
# df['200 day sma'] = sma200d.df
# rsi = btalib.rsi(df)
# df['rsi'] = rsi.df
# macd = btalib.macd(df)
# df['macd'] = macd.df['macd']
# df['signal'] = macd.df['signal']
# df['histogram'] = macd.df['histogram']
# print(df)
# # f = open('data/ohlc/AAPL.txt', 'w+')
# # f.write(df)
# df.to_csv(path_or_buf='data/ohlc/AAPL.txt', index='Date')

##########################################################

# now = datetime.now()
# dt = now.strftime('%y-%m-%d')
# print(dt)
# f = open('Status/LastDayScan.txt', 'r')
# # print(f.read())
# lastScan = f.read()
# print(lastScan)
# if(lastScan != dt):
#     print('they diff')
# else:
#     print('they same')

##########################################################

# symbols = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA', 'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', 'OKTA', 'TWTR', 'TM', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM']
# # tickers is needed to trim [] & ''
# tickers = ','.join(symbols)
# # get data using the same method as OHLC.getDailyData()
# FvtMinBarUrl = '{}/5Min?symbols={}&limit=20'.format(config.BARS_URL, tickers)
# r = requests.get(FvtMinBarUrl, headers=config.HEADERS)
# data = r.json()
# for symbol in data:
#     filename = 'data/15MinOHLC/{}.txt'.format(symbol)
#     f = open(filename, 'w+')
#     f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
#     for bar in data[symbol]:
#         t = datetime.fromtimestamp(bar['t'])
#         day = t.strftime('%Y-%m-%d')
#         line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
#         f.write(line)
# f.close()
# print('Fetched 15 minute data from alpaca api')

##########################################################

# symbols = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA', 'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', 'OKTA', 'TWTR', 'TM', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM']
# # # tickers is needed to trim [] & ''
# tickers = ','.join(symbols)
# get list of tickers to open and scan files
# read data and determine if there is a buy signal
# open daily file, read, and compare 200 day sma with 5 day sma
# for symbol in symbols:
#     print(symbol)
#     file = open('data/DayOHLC/{}.txt'.format(symbol))
#     print(file.read())
# gather all buy signals to send to alpaca through Orders.submitOrder(self, qty, stock, side, resp)

##########################################################

# FvtMinBarUrl = '{}/15Min?symbols={}&limit=2'.format(config.BARS_URL, tickers)
# r = requests.get(FvtMinBarUrl, headers=config.HEADERS)
# data = r.json()
# # print(json.dumps(r.json(), indent=4))
# for symbol in data:
#     filename = 'data/15MinOHLC/{}.json'.format(symbol)
#     f = open(filename, 'w+')
#     f.write('{' + '"{}": '.format(symbol) + json.dumps(data[symbol], indent=4) + '}')
#     f.close()
# print('Fetched 15 minute data from alpaca api')

##########################################################

# get list of tickers to open and scan files
# read data and determine if there is a buy signal
# open daily file, read, and compare 200 day sma with 5 day sma
long = []
short = []
#dayLessOne = datetime.today()- timedelta(days=1)
#dt = dayLessOne.strftime('%Y-%m-%d')
dt = datetime.today()
#print(dt)
dtt = dt.strftime('%Y-%m-%d')
for symbol in symbols:
    df = pd.read_csv('data/DayOHLC/{}.txt'.format(symbol), parse_dates=True) #, index_col='Date'
    a = df.loc[(df['Date'] == dt), ('5 day sma')].values
    b = df.loc[(df['Date'] == dt), ('200 day sma')].values
    # gather all buy signals to send to alpaca through Orders.submitOrder(self, qty, stock, side, resp)
    if(a < b):
        with open('data/15MinOHLC/{}.json'.format(symbol)) as f:
            data = json.load(f)
            list=data['{}'.format(symbol)]
            cData = list[1].get('c')
            hData = list[1].get('h')
            oData = list[1].get('o')
            if((cData > oData) and ((cData / hData) > 0.95)):
                print('buy/long signal')
                long.append(symbol)
            else:
                print('not a signal')
    else:
        with open('data/15MinOHLC/{}.json'.format(symbol)) as f:
            data = json.load(f)
            list=data['{}'.format(symbol)]
            cData = list[1].get('c')
            lData = list[1].get('l')
            oData = list[1].get('o')
            if((oData > cData) and (cData / lData) > 0.95):
                print('sell/short signal')
                short.append(symbol)
            else:
                print('not a signal')

print(long)
print(short)

##########################################################

