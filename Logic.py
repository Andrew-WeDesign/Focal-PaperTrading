import pandas as pd
import btalib
import json
import Orders
from datetime import datetime, timedelta
import alpaca_trade_api as tradeapi
import requests
import config

def newPosLogic(self, symbols):
    self.long = []
    self.short = []
    positions = self.alpaca.list_positions()
    blacklist = set()
    for position in positions:
        blacklist.add(position.symbol)
    dt = datetime.today()
    lastOpenDay = dt.strftime('%Y-%m-%d')
    for symbol in config.symbols:
        if(blacklist.isdisjoint({symbol})):
            df = pd.read_csv('Data/15MinOHLC/{}.txt'.format(symbol), parse_dates=True) #, index_col='Date'
            a = df.loc[(df['Date'] == lastOpenDay), ('rsi')].values
            b = df.loc[(df['Date'] == lastOpenDay), ('stoc k')].values
            c = df.loc[(df['Date'] == lastOpenDay), ('stoc d')].values
            d = df.loc[(df['Date'] == lastOpenDay), ('macd')].values
            e = df.loc[(df['Date'] == lastOpenDay), ('signal')].values

            if ((a < 35) and (b < 25) and (c < 25) and (d > e)):
                print('buy signal for {}'.format(symbol))
                self.long.append(symbol)
            elif((a > 65) and (b > 75) and (c > 75) and (d < e)):
                print('sell signal for {}'.format(symbol))
                self.short.append(symbol)
        else:
            print('symbol is in an open position, not placing new position')
    Orders.orderSize(self, self.long, self.short)


def curPosLogic(self):
    dt = datetime.today()
    tDelta = timedelta(days=1)
    dtLessOne = dt - tDelta
    day = dt.strftime('%Y-%m-%d')
    dayLessOne = dtLessOne.strftime('%Y-%m-%d')
    positions = self.alpaca.list_positions()
    for position in positions:
        df = pd.read_csv('data/15MinOHLC/{}.txt'.format(position.symbol), parse_dates=True)
        a = df.loc[(df['Date'] == day), ('rsi')].values
        b = df.loc[(df['Date'] == day), ('stoc k')].values
        c = df.loc[(df['Date'] == day), ('stoc d')].values
        d = df.loc[(df['Date'] == day), ('macd')].values
        e = df.loc[(df['Date'] == day), ('signal')].values
        # d = df.loc[(df['Date'] == day), ('histogram')].values
        # e = df.loc[(df['Date'] == dayLessOne), ('histogram')].values
        purchasePrice = float(position.avg_entry_price)
        currentPrice = float(position.current_price)
        if(position.side == 'long'):
            if((a > 65) and (b > 75) and (c > 75)):
                print('sell/exit signal for long position in {}'.format(position.symbol))
                qty = int(position.qty)
                Orders.submitOrder(self, qty, position.symbol, 'sell')
            # may later replace with a trailing stop loss, but the macd might be an earlier warning than a stop loss
            # elif(d < e):
            #     print('macd is crossing exit position for {}'.format(position.symbol))
            #     qty = int(position.qty)
            #     Orders.submitOrder(self, qty, position.symbol, 'sell')
            elif((currentPrice/purchasePrice) > 1.015):
                print('closing {} position to realize gains'.format(position.symbol))
                qty = int(position.qty)
                Orders.submitOrder(self, qty, position.symbol, 'sell')
            elif((currentPrice/purchasePrice) < 1):
                print('closing {} position to stop losses'.format(position.symbol))
                qty = int(position.qty)
                Orders.submitOrder(self, qty, position.symbol, 'sell')
            else:
                print('holding position {} {} {}'.format(position.symbol, position.qty, position.side))
        elif(position.side == 'short'):
            if((a < 35) and (b < 25) and (c < 25)):
                print('buy/exit signal for short position in {}'.format(position.symbol))
                qty = abs(int(position.qty))
                Orders.submitOrder(self, qty, position.symbol, 'buy')
            # may later replace with a trailing stop loss, but the macd might be an earlier warning than a stop loss
            # elif(e < d):
            #     print('macd is crossing exit position for {}'.format(position.symbol))
            #     qty = abs(int(position.qty))
            #     Orders.submitOrder(self, qty, position.symbol, 'buy')
            elif((purchasePrice/currentPrice) > 1.015):
                print('closing {} position to realize gains'.format(position.symbol))
                qty = abs(int(position.qty))
                Orders.submitOrder(self, qty, position.symbol, 'buy')
            elif((purchasePrice/currentPrice) < 1):
                print('closing {} position to stop losses'.format(position.symbol))
                qty = abs(int(position.qty))
                Orders.submitOrder(self, qty, position.symbol, 'buy')
            else:
                print('holding position {} {} {}'.format(position.symbol, position.qty, position.side))

