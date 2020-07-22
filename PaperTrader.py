import requests, json, sys
import alpaca_trade_api as tradeapi
import PaperConfig
# from PaperConfig import * # contains api keys

# FiveMinBarUrl = PaperConfig.BARS_URL + '/5Min?symbols=MSFT'
# r = requests.get(FiveMinBarUrl, headers=PaperConfig.HEADERS)

symbols = 'AAPL'
day_bars_url = '{}/day?symbols={}&limit=1000'.format(PaperConfig.BARS_URL, symbols)
r = requests.get(day_bars_url, headers=PaperConfig.HEADERS)
print(r)

r = requests.get('https://data.alpaca.markets/v1/bars/day?symbols=AAPL', headers=PaperConfig.HEADERS)
print(r)
# symbols = 'MSFT'
# FiveMinBarUrl = '{}/day?symbols={}&limit=1000'.format(PaperConfig.BARS_URL, symbols)
# r = requests.get(FiveMinBarUrl, headers=PaperConfig.HEADERS)

# print(json.dumps(r.json(), indent = 4))

# original_stdout = sys.stdout
# with open('ta.txt', 'w') as f:
#     sys.stdout = f
#     print(r)
#     sys.stdout = original_stdout