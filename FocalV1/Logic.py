import pandas as pd
import btalib
import json
import Orders
from datetime import datetime, timedelta

def buyLogic(self, symbols):
    # get list of tickers to open and scan files
    # read data and determine if there is a buy signal
    # open daily file, read, and compare 200 day sma with 5 day sma
    self.long = []
    self.short = []
    #dayLessOne = datetime.today()- timedelta(days=1)
    #dt = dayLessOne.strftime('%Y-%m-%d')
    dt = datetime.today()
    for symbol in self.symbols:
        df = pd.read_csv('data/DayOHLC/{}.txt'.format(symbol), parse_dates=True) #, index_col='Date'
        a = df.loc[(df['Date'] == dt), ('5 day sma')].values
        b = df.loc[(df['Date'] == dt), ('20 day sma')].values
        # gather all buy signals to send to alpaca through Orders.submitOrder(self, qty, stock, side, resp)
        if(a < b):
            with open('data/15MinOHLC/{}.json'.format(symbol)) as f:
                data = json.load(f)
                list=data['{}'.format(symbol)]
                cData = list[1].get('c')
                hData = list[1].get('h')
                oData = list[1].get('o')
                if((cData > oData) and ((cData / hData) > 0.95)):
                    print('placing a long order for {}'.format(symbol))
                    self.long.append(symbol)
                else:
                    print('not a long signal')
        else:
            with open('data/15MinOHLC/{}.json'.format(symbol)) as f:
                data = json.load(f)
                list=data['{}'.format(symbol)]
                cData = list[1].get('c')
                lData = list[1].get('l')
                oData = list[1].get('o')
                if((oData > cData) and ((cData / lData) > 0.98)):
                    print('placing a short order for {}'.format(symbol))
                    self.short.append(symbol)
                else:
                    print('not a short signal')
    Orders.orderSize(self, self.long, self.short)
