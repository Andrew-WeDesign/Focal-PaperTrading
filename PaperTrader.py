import requests
import json
import btalib
import config
import OHLC
from datetime import datetime
import pandas as pd
import alpaca_trade_api as tradeapi

class AlgoTrader:
    # update data at the start of program
    def __init__(self):
        # list of all stock tickers we want to track
        self.symbols = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA',
        'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW',
        'OKTA', 'TWTR', 'TM', 'RTN', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM']
        # tickers is needed to trim [] & ''
        self.tickers = ','.join(self.symbols)

    def run(self):
        # check to see if the day to day data is up to date
        dateNow = datetime.now()
        dateT = dateNow.strftime('%Y-%m-%d')
        g = open('Status/LastDayScan.txt', 'r')
        lastScan = g.read()
        g.close()
        if(lastScan != dateT):
            print('Daily data is out of date, updating data.')
            OHLC.getDailyData(self)
            g = open('Status/LastDayScan.txt', 'w+')
            g.write(dateT)
            g.close()
        else:
            print('Daily data is up to date.')

        print('end of run')


ls = AlgoTrader()
ls.run()