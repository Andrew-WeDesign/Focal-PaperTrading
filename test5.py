import btalib
import pandas as pd
import config
import requests
import json
from datetime import datetime, timedelta
import alpaca_trade_api as tradeapi

#alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')
alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')
tickers = ','.join(config.symbols)

#r = alpaca.get_account()
#print(tickers)
dayBarsUrl = '{}/1Min?symbols={}&limit=200'.format(config.BARS_URL, tickers)
r = requests.get('https://data.alpaca.markets/v1/bars/15Min?symbols=AAPL,MSFT&limit=120', headers=config.HEADERS)
#json.dumps(r)
print(r.content)