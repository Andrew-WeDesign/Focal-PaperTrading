import requests
import json
import btalib
import config
import OHLC
import MarketHours
import Orders
import Logic
import time
from datetime import datetime
import pandas as pd
import alpaca_trade_api as tradeapi

class AlgoTrader:
    # update data at the start of program
    def __init__(self):
        self.alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')

        # list of all stock tickers we want to track
        self.symbols = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA',
        'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW',
        'OKTA', 'TWTR', 'TM', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM', 'FANG', 
        'MXIM', 'JKHY', 'KEYS', 'FTNT', 'ROL', 'ANET', 'CPRT', 'FLT', 'HFC', 'BR', 
        'TWTR', 'EVRG', 'ABMD', 'MSCI', 'TTWO', 'SIVB', 'IPGP', 'HII', 'NCLH', 'CDNS', 
        'SBAC', 'IQV', 'MGM', 'RMD', 'AOS', 'PKG', 'DRE', 'BKR', 'HLT', 'RE']
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

        while True:
            # check if market is open, if not then wait
            MarketHours.marketHours(self)

            # cancel all open orders
            orders = self.alpaca.list_orders(status="open")
            for order in orders:
                self.alpaca.cancel_order(order.id)
            
            # close all positions
            Orders.closePositions(self)

            # get new data for 15 minute intervals
            OHLC.getFvtMinData(self)

            # apply algorithm for buy orders
            # currently we will simply sell all orders at the beginning of the 5 minute mark, but apply logic for selling later
            Logic.buyLogic(self, self.symbols)
            print('Next loop will run in 5 minutes.')
            time.sleep(300)

        print('end of run')


ls = AlgoTrader()
ls.run()