import config
import requests
import json
import alpaca_trade_api as tradeapi

alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')
# tickers is needed to trim [] & '' off symbols
tickers = ','.join(config.symbols)


OneMinBarUrl = '{}/1Min?symbols={}&limit=120'.format(config.BARS_URL, tickers)
r = requests.get(OneMinBarUrl, headers=config.HEADERS)
data = r.json()
for symbol in data:
    filename = 'data/1MinOHLC/{}.json'.format(symbol)
    f = open(filename, 'w+')
    f.write('{' + '"{}": '.format(symbol) + json.dumps(data[symbol], indent=4) + '}')
    # to save as csv comment out the line above, and uncomment the block below
    # decided to save info as json. This block transforms it into csv
    ################################################################
    # f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
    # for bar in data[symbol]:
    #     t = datetime.fromtimestamp(bar['t'])
    #     day = t.strftime('%Y-%m-%d')
    #     line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
    #     f.write(line)
    ################################################################
    f.close()
print('Fetched one minute data from alpaca api')