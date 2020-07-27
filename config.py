API_KEY = 'PK24DPNBTW93BURSH6KR'
SECRET_KEY = 'm34lUIrYuHImdnAvoV7jE6BsE7G5yVPAdtiGImHA'
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY} #required for each request

BASE_URL = 'https://paper-api.alpaca.markets' #the main endpoint for requests
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL) #endpoint for account details
ORDERS_URL = '{}/v2/orders'.format(BASE_URL) #endpoint for orders
LIST_POSITIONS = '{}/v2/positions'.format(BASE_URL) #endpoint for all open positions

BARS_URL = 'https://data.alpaca.markets/v1/bars'

# list of all stock tickers we want to track
symbols = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA', 
'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', #9
'OKTA', 'TM', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM', 'FANG', 
'MXIM', 'JKHY', 'KEYS', 'FTNT', 'ROL', 'ANET', 'CPRT', 'FLT', 'HFC', 'BR', 
'TWTR', 'EVRG', 'ABMD', 'MSCI', 'TTWO', 'SIVB', 'IPGP', 'HII', 'NCLH', 'CDNS', 
'SBAC', 'IQV', 'MGM', 'RMD', 'AOS', 'PKG', 'DRE', 'BKR', 'HLT', 'RE', 
'OCUL', 'EVRI', 'FNKO', 'HEAR', 'FIT', 'BABA', 'F', 'SBUX', #8
'NGM', 'FLXN', 'VKTX', 'CHNG', 'EPD', 'ELY', 'VST', 'MTNB', #8
'BTG', 'GDP', 'PFNX', 'CECE'] #4

# axed symbols: CFPZF ARDS CHPRF CRPB GELYF TCNNF TDS PROSY GOPRO TWTR