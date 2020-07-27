import requests
import json
import btalib
import time
from datetime import datetime
import pandas as pd
import alpaca_trade_api as tradeapi
import config
import MarketHours
import Logic
import DataGather
import Orders

class AlgoTrader:
    # update data at the start of program
    def __init__(self):
        self.alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')
        # tickers is needed to trim [] & '' off symbols
        self.tickers = ','.join(config.symbols)

    def run(self):
        # get day by day data that will not have updates throughout the day
        DataGather.startOfDay(self)
        while True:
            # check for market open
            MarketHours.isOpen(self)
            # cancel any open orders
            self.alpaca.cancel_all_orders()
            # get new data 
            DataGather.getOneMinData(self)
            # algorithm for current positions
            Logic.curPosLogic(self)
            # algorithm for new positions
            Logic.newPosLogic(self, self.symbols)
            print('Next loop will run in 1 minutes')
            time.sleep(60)
        print('end of run')


ls = AlgoTrader()
ls.run()