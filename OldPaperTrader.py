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

##################################################################
#get request for account data associated with API keys in PaperConfig
def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

#creates a new order
def create_order(symbol, qty, side, type, time_in_force):
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": type,
            "time_in_force": time_in_force
        }

        r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
        
        return json.loads(r.content)

#returns a list of all orders
def get_orders():
        r = requests.get(ORDERS_URL, headers=HEADERS)
        
        return json.loads(r.content)
##################################################################



##################################################################
#creates order - codes need to be in order (AMZN = symbol etc).
#response = create_order("AAPL", 1, "buy", "market", "gtc") 
#response = create_order("MSFT", 10, "buy", "market", "gtc")

#prints out the content of response
#print(response)

#pulls get_orders data and prints it
orders = get_orders()
print(orders)

#pulls account data and prints it
account_details = get_account()
print(account_details)
##################################################################