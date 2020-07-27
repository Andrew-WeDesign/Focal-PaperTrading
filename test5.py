import btalib
import pandas as pd
import config
import requests
import json
from datetime import datetime, timedelta
import alpaca_trade_api as tradeapi

alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')

#r = alpaca.get_account()
r = alpaca.list_positions()
print(r)