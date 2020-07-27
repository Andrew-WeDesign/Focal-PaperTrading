import alpaca_trade_api as tradeapi
import requests
import json
import config

#def closePositions(self):
alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')

positions = alpaca.list_positions()
for position in positions:
    if(position.side == 'long'):
        side = 'sell'
    else:
        side = 'buy'
    symbol = position.symbol
    qty = position.qty
    qty = abs(int(qty))
    #alpaca.submit_order(symbol, qty, side, "market", "day")
    print("Market order of | " + str(qty) + " " + symbol + " " + side + " | completed.")
print(positions)
print('end of part 1')
positions = requests.get('https://paper-api.alpaca.markets/v2/positions', headers = config.HEADERS)
print(positions)
#submitOrder(self, qty, symbol, side)
# if(int(qty) > 0):
#     try:
#         alpaca.submit_order(symbol, qty, side, "market", "day")
#         print("Market order of | " + str(qty) + " " + symbol + " " + side + " | completed.")
        
#     except:
#         print("Order of | " + str(qty) + " " + symbol + " " + side + " | did not go through.")
            
# else:
#         print("Quantity is 0, order of | " + str(qty) + " " + symbol + " " + side + " | not completed.")