import requests, json
import threading
import time
import datetime
import alpaca_trade_api as tradeapi
from PaperConfig import * #contains api keys

BASE_URL = "https://paper-api.alpaca.markets" #the main endpoint for requests
ACCOUNT_URL = "{}/v2/account".format(BASE_URL) #endpoint for account details
ORDERS_URL = "{}/v2/orders".format(BASE_URL) #endpoint for orders
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY} #required for each request
