import btalib
import pandas as pd
from datetime import datetime

# df = pd.read_csv('data/ohlc/AAPL.txt', parse_dates=True, index_col='Date')
# sma5d = btalib.sma(df, period=5)
# df['5 day sma'] = sma5d.df
# sma200d = btalib.sma(df, period=200)
# df['200 day sma'] = sma200d.df
# rsi = btalib.rsi(df)
# df['rsi'] = rsi.df
# macd = btalib.macd(df)
# df['macd'] = macd.df['macd']
# df['signal'] = macd.df['signal']
# df['histogram'] = macd.df['histogram']
# print(df)

# # f = open('data/ohlc/AAPL.txt', 'w+')
# # f.write(df)
# df.to_csv(path_or_buf='data/ohlc/AAPL.txt', index='Date')
##########################################################
now = datetime.now()
dt = now.strftime('%y-%m-%d')
print(dt)
f = open('Status/LastDayScan.txt', 'r')
# print(f.read())
lastScan = f.read()
print(lastScan)
if(lastScan != dt):
    print('they diff')
else:
    print('they same')
##########################################################
