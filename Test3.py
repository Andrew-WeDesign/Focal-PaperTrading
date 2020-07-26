import config
import alpaca_trade_api as tradeapi
import json
import requests
import time
from datetime import datetime, timedelta

alpaca = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version = 'v2')

# positions = alpaca.list_positions()
# #print(positions[1])
# openPos = []
# for position in positions:
#     # print(position)
#     a = position.symbol
#     print(a)
#     openPos.append(a)
#     # b = json.dumps(a,indent=4)
#     # print(type(b))

# #print(openPos)
########################################################
# dt = datetime.today()
# tDelta = dt - timedelta(days = 4)
# dt = dt.strftime('%Y-%m-%d')
# tDelta = tDelta.strftime('%Y-%m-%d')
# calEnd = datetime.today()
# tDelta = timedelta(days=7)
# calStart = calEnd - tDelta
# calEnd = calEnd.strftime('%Y-%m-%d')
# calStart = calStart.strftime('%Y-%m-%d')
# print(calStart)
# print(calEnd)
# calendar = alpaca.get_calendar(start=calStart, end=calEnd)
# print(calendar[-1].date)
# lastOpenDay = calendar[-1].date
# lastOpenDay = lastOpenDay.strftime('%Y-%m-%d')
# print(lastOpenDay)
########################################################
long = []
short = []
for symbol in config.symbols:
    with open('data/1MinOHLC/{}.json'.format(symbol)) as f:
        data = json.load(f)
        list=data['{}'.format(symbol)]
        cData = list[119].get('c')
        hData = list[119].get('h')
        oData = list[119].get('o')
        if((cData > oData) and ((cData / hData) < 1.1)):
            print('placing a long order for {}'.format(symbol))
            long.append(symbol)
        else:
            print('not a long signal')