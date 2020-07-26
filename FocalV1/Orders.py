import alpaca_trade_api as tradeapi
import requests
import json

def submitOrder(self, qty, symbol, side):
    if(isinstance(qty, int)):
        if(qty >= 1):
            try:
                self.alpaca.submit_order(symbol, qty, side, "market", "day")
                print("Market order of | " + str(qty) + " " + symbol + " " + side + " | completed.")
                
            except:
                print("Order of | " + str(qty) + " " + symbol + " " + side + " | did not go through.")
                
        else:
            print("Quantity is 0, order of | " + str(qty) + " " + symbol + " " + side + " | not completed.")
        

def orderSize(self, long, short):
    equity = int(float(self.alpaca.get_account().equity))
    self.shortAmount = equity * 0.30
    self.longAmount = equity - self.shortAmount
    if(len(long) != 0):
        longSplit = self.longAmount / len(long)
    if(len(short) != 0):
        shortSplit = self.shortAmount / len(short)

    for symbol in long:
        print('long position taken in {}'.format(symbol))
        with open('data/15MinOHLC/{}.json'.format(symbol)) as f:
                data = json.load(f)
                list=data['{}'.format(symbol)]
                cData = list[1].get('c')
        qty = int(float(longSplit / cData))
        side = 'buy'
        submitOrder(self, qty, symbol, side)
        
    for symbol in short:
        print('short position taken in {}'.format(symbol))
        with open('data/15MinOHLC/{}.json'.format(symbol)) as f:
            data = json.load(f)
            list=data['{}'.format(symbol)]
            cData = list[1].get('c')
        qty = int(float(shortSplit / cData))
        side = 'sell'
        submitOrder(self, qty, symbol, side)

def closePositions(self):
    positions = self.alpaca.list_positions()
    for position in positions:
        if(position.side == 'long'):
            side = 'sell'
        else:
            side = 'buy'
        symbol = position.symbol
        qty = abs(int(position.qty))
        submitOrder(self, qty, symbol, side)