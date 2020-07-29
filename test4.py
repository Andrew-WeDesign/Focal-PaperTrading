import config
import requests
import json
import alpaca_trade_api as tradeapi
import pandas as pd
from datetime import datetime, timedelta
import Orders

alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')
# tickers is needed to trim [] & '' off symbols
tickers = ','.join(config.symbols)

# def newPositionLogic(self, symbols):
# self.long = []
# self.short = []
# positions = self.alpaca.list_positions()
# blacklist = set()
# for position in positions:
#     blacklist.add(position.symbol)
# dt = datetime.today()
# lastOpenDay = dt.strftime('%Y-%m-%d')
# for symbol in config.symbols:
#     if(blacklist.isdisjoint({symbol})):
#         df = pd.read_csv('Data/15MinOHLC/{}.txt'.format(symbol), parse_dates=True) #, index_col='Date'
#         a = df.loc[(df['Date'] == lastOpenDay), ('rsi')].values
#         b = df.loc[(df['Date'] == lastOpenDay), ('stoc k')].values
#         c = df.loc[(df['Date'] == lastOpenDay), ('stoc d')].values
#         if ((a < 30)and (b < 20) and(c < 20)):
#             print('buy signal for {}'.format(symbol))
#             self.long.append(symbol)
#         elif((a > 70) and (b > 80) and (c > 80)):
#             print('sell signal for {}'.format(symbol))
#             self.short.append(symbol)
#     else:
#         print('symbol is in an open position, not placing new position')
# Orders.orderSize(self, self.long, self.short)

dt = datetime.today()
lastOpenDay = dt.strftime('%Y-%m-%d')
positions = self.alpaca.list_positions()
for position in positions:
    df = pd.read_csv('data/15MinOHLC/{}.txt'.format(position.symbol), parse_dates=True)
    a = df.loc[(df['Date'] == lastOpenDay), ('rsi')].values
    b = df.loc[(df['Date'] == lastOpenDay), ('stoc k')].values
    c = df.loc[(df['Date'] == lastOpenDay), ('stoc d')].values
    if(position.side == 'long'):
        if((a > 70) and (b > 80) and (c > 80)):
            print('sell signal for {}'.format(position.symbol))
            qty = int(position.qty)
            Orders.submitOrder(self, qty, position.symbol, 'sell')
    elif(position.side == 'short'):
        if((a < 30)and (b < 20) and(c < 20)):
            print('buy signal for {}'.format(position.symbol))
            qty = int(position.qty)
            Orders.submitOrder(self, qty, position.symbol, 'buy')
    else:
        print('holding position {} {} {}'.format(position.symbol, position.qty, position.side))

def curPosLogic(self):
    dt = datetime.today()
    dt = dt.strftime('%Y-%m-%d')
    positions = self.alpaca.list_positions()
    for position in positions:
        df = pd.read_csv('data/15MinOHLC/{}.txt'.format(position.symbol), parse_dates=True)
        macd = df.loc[(df['Date'] == dt), ('macd')].values
        macdSignal = df.loc[(df['Date'] == dt), ('signal')].values
        if(position.side == 'long'):
            purchasePrice = float(position.avg_entry_price)
            currentPrice = float(position.current_price)
            if(macd < macdSignal):
                print('long position should be closed due to cross on macd')
                qty = int(position.qty)
                Orders.submitOrder(self, qty, position.symbol, 'sell')
            elif((currentPrice/purchasePrice) > 1.02):
                print('closing {} position to realize gains'.format(position.symbol))
                qty = int(position.qty)
                # Orders.submitOrder(self, qty, position.symbol, 'sell')
            elif((currentPrice/purchasePrice) < 0.99):
                print('closing {} position to realize losses'.format(position.symbol))
                qty = int(position.qty)
                # Orders.submitOrder(self, qty, position.symbol, 'sell')
            else:
                print('holding position {} {} {}'.format(position.symbol, position.qty, position.side))
        elif(position.side == 'short'):
            purchasePrice = abs(float(position.avg_entry_price))
            currentPrice = abs(float(position.current_price))
            if(macd > macdSignal):
                print('short position should be closed due to cross on macd')
                qty = abs(int(position.qty))
                # Orders.submitOrder(self, qty, position.symbol, 'buy')
            elif((purchasePrice/currentPrice) > 1.02):
                print('closing {} position to realize gains'.format(position.symbol))
                qty = abs(int(position.qty))
                # Orders.submitOrder(self, qty, position.symbol, 'buy')
            elif((purchasePrice/currentPrice) < 0.99):
                print('closing {} position to realize losses'.format(position.symbol))
                qty = abs(int(position.qty))
                # Orders.submitOrder(self, qty, position.symbol, 'buy')
            else:
                print('holding position {} {} {}'.format(position.symbol, position.qty, position.side))


# def newPosLogic(self, symbols):
#     self.long = []
#     self.short = []
#     positions = self.alpaca.list_positions()
#     blacklist = set()
#     for position in positions:
#         blacklist.add(position.symbol)
#     dt = datetime.today()
#     lastOpenDay = dt.strftime('%Y-%m-%d')
#     for symbol in config.symbols:
#         if(blacklist.isdisjoint({symbol})):
#             df = pd.read_csv('data/1MinMACD/{}.txt'.format(symbol), parse_dates=True) #, index_col='Date'
#             a = df.loc[(df['Date'] == lastOpenDay), ('macd')].values
#             b = df.loc[(df['Date'] == lastOpenDay), ('signal')].values
#             if(a > b):
#                 with open('data/1MinOHLC/{}.json'.format(symbol)) as f:
#                     data = json.load(f)
#                     list=data['{}'.format(symbol)]
#                     cData = list[-1].get('c')
#                     hData = list[-1].get('h')
#                     oData = list[-1].get('o')
#                     if((cData > oData) and ((cData / hData) < 1.1)):
#                         print('placing a long order for {}'.format(symbol))
#                         self.long.append(symbol)
#                     else:
#                         print('not a long signal')
#             elif(b > a):
#                 with open('data/1MinOHLC/{}.json'.format(symbol)) as f:
#                     data = json.load(f)
#                     list=data['{}'.format(symbol)]
#                     cData = list[-1].get('c')
#                     lData = list[-1].get('l')
#                     oData = list[-1].get('o')
#                     if((oData > cData) and ((cData / lData) > 0.9)):
#                         print('placing a short order for {}'.format(symbol))
#                         self.short.append(symbol)
#                     else:
#                         print('not a short signal')
#         else:
#             print('symbol is in an open position, not placing new position')
#     # Orders.orderSize(self, self.long, self.short)

