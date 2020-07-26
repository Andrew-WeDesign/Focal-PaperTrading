import pandas as pd
import btalib
import json
import Orders
from datetime import datetime, timedelta

def newPosLogic(self, symbols):
    # get list of tickers to open and scan files
    # read data and determine if there is a long/short signal
    # open daily file, read, and compare macd
    self.long = []
    self.short = []
    # get list of open positions, so if a position is open it doesn't enter more
    positions = self.alpaca.list_position()
    blacklist = []
    for position in positions:
        blacklist.append(position.symbol)
    calEnd = datetime.today()
    tDelta = timedelta(days=7)
    calStart = calEnd - tDelta
    calEnd = calEnd.strftime('%Y-%m-%d')
    calStart = calStart
    calendar = self.alpaca.alpaca.get_calendar(start=calStart, end=calEnd)
    lastOpenDay = calendar[-1].date
    lastOpenDay = lastOpenDay.strftime('%Y-%m-%d')
    for symbol in self.symbols:
        if(blacklist.isdisjoint(symbol)):
            df = pd.read_csv('data/DayOHLC/{}.txt'.format(symbol), parse_dates=True) #, index_col='Date'
            a = df.loc[(df['Date'] == lastOpenDay), ('macd')].values
            b = df.loc[(df['Date'] == lastOpenDay), ('signal')].values
            # gather all buy signals to send to alpaca through Orders.submitOrder(self, qty, stock, side, resp)
            if(a > b):
                with open('data/1MinOHLC/{}.json'.format(symbol)) as f:
                    data = json.load(f)
                    list=data['{}'.format(symbol)]
                    cData = list[119].get('c')
                    hData = list[119].get('h')
                    oData = list[119].get('o')
                    if((cData > oData) and ((cData / hData) > 0.90)):
                        print('placing a long order for {}'.format(symbol))
                        self.long.append(symbol)
                    else:
                        print('not a long signal')
            else:
                with open('data/1MinOHLC/{}.json'.format(symbol)) as f:
                    data = json.load(f)
                    list=data['{}'.format(symbol)]
                    cData = list[119].get('c')
                    lData = list[119].get('l')
                    oData = list[119].get('o')
                    if((oData > cData) and ((cData / lData) > 0.98)):
                        print('placing a short order for {}'.format(symbol))
                        self.short.append(symbol)
                    else:
                        print('not a short signal')
        else:
            print('symbol is in an open position, not placing new position')
    Orders.orderSize(self, self.long, self.short)

def curPosLogic(self):
    dt = datetime.today()
    dt = dt.strftime('%Y-%m-%d')
    positions = self.alpaca.list_position()
    for position in positions:
        df = pd.read_csv('data/DayOHLC/{}.txt'.format(position.symbol), parse_dates=True)
        macd = df.loc[(df['Date'] == dt), ('macd')].values
        macdSignal = df.loc[(df['Date'] == dt), ('signal')].values
        if(position.side == 'long'):
            purchasePrice = float(position.avg_entry_price)
            currentPrice = float(position.current_price)
            if(macd < macdSignal):
                print('long position should be closed due to cross on macd')
                Orders.submitOrder(self, position.qty, position.symbol, 'sell')
            elif((currentPrice/purchasePrice) > 1.02):
                print('closing position to realize gains')
                Orders.submitOrder(self, position.qty, position.symbol, 'sell')
            else:
                print('holding position {} {} {}'.format(position.symbol, position.qty, position.side))
        elif(position.side == 'short'):
            purchasePrice = abs(float(position.avg_entry_price))
            currentPrice = abs(float(position.current_price))
            if(macd > macdSignal):
                print('short position should be closed due to cross on macd')
                Orders.submitOrder(self, position.qty, position.symbol, 'buy')
            elif((purchasePrice/currentPrice) > 1.02):
                print('closing position to realize gains')
                Orders.submitOrder(self, position.qty, position.symbol, 'buy')
            else:
                print('holding position {} {} {}'.format(position.symbol, position.qty, position.side))
