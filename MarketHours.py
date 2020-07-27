import requests
import json
import time
import datetime
import alpaca_trade_api as tradeapi
import config
import Orders
import Logic

def isOpen(self):
    # Wait for market to open.
    print("Waiting for market to open...")
    awaitMarketOpen(self)
    # tAMO = threading.Thread(target=self.awaitMarketOpen)
    # tAMO.start()
    # tAMO.join()
    print("Market opened.")
    # Figure out when the market will close so we can prepare to sell beforehand.
    clock = self.alpaca.get_clock()
    closingTime = clock.next_close.replace(tzinfo=datetime.timezone.utc).timestamp()
    currTime = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
    self.timeToClose = closingTime - currTime
# TODO: leaving this for now, may be removed later
    if(self.timeToClose < (60 * 16)):
        # Close all positions when 15 minutes til market close.
        print("Market closing soon.  Closing positions.")
        positions = self.alpaca.list_positions()
        for position in positions:
            if(position.side == 'long'):
                orderSide = 'sell'
            else:
                orderSide = 'buy'
            qty = abs(int(float(position.qty)))
            # qty = position.qty
            # respSO = []
            Orders.submitOrder(self, qty, position.symbol, orderSide)
            # tSubmitOrder = threading.Thread(target=self.submitOrder(qty, position.symbol, orderSide, respSO))
            # tSubmitOrder.start()
            # tSubmitOrder.join()

def awaitMarketOpen(self):
    isOpen = self.alpaca.get_clock().is_open
    while(not isOpen):
        clock = self.alpaca.get_clock()
        openingTime = clock.next_open.replace(tzinfo=datetime.timezone.utc).timestamp()
        currTime = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
        timeToOpen = int((openingTime - currTime) / 60)
        print(str(timeToOpen) + " minutes til market open.")
        time.sleep(60)
        isOpen = self.alpaca.get_clock().is_open