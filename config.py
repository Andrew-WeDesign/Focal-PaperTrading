API_KEY = 'PKDVOQB89S2RLI6Y64F6'
SECRET_KEY = 'NSTMFEb24TsGGeWBgFat6sNPGwy9lHMmxu65ZfS/'
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY} #required for each request

BASE_URL = 'https://paper-api.alpaca.markets' #the main endpoint for requests
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL) #endpoint for account details
ORDERS_URL = '{}/v2/orders'.format(BASE_URL) #endpoint for orders
LIST_POSITIONS = '{}/v2/positions'.format(BASE_URL) #endpoint for all open positions

BARS_URL = 'https://data.alpaca.markets/v1/bars'

# list of all stock tickers we want to track
symbols = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA', 
'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', 'MMM', 
'OKTA', 'TM', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM', 'FANG', 
'MXIM', 'JKHY', 'KEYS', 'FTNT', 'ROL', 'ANET', 'CPRT', 'FLT', 'HFC', 'BR', 
'TWTR', 'EVRG', 'ABMD', 'MSCI', 'TTWO', 'SIVB', 'IPGP', 'HII', 'NCLH', 'CDNS', 
'SBAC', 'IQV', 'MGM', 'RMD', 'AOS', 'PKG', 'DRE', 'BKR', 'HLT', 'RE', 
'OCUL', 'EVRI', 'EA', 'FFIV', 'FB', 'BABA', 'F', 'SBUX', 'ABT', 'ABBV', 
'NGM', 'FLXN', 'VKTX', 'CHNG', 'EPD', 'ELY', 'VST', 'MTNB', 'ACN', 'ADBE', 
'BTG', 'GDP', 'PFNX', 'CECE', 'AMD', 'AAP', 'AES', 'AFL', 'A', 'APD', 
'AKAM', 'ALK', 'ALB', 'ARE', 'GOOG', 'GOOGL', 'AEP', 'AXP', 'ANTM', 'APA', 
'T', 'BBY', 'COG', 'COF', 'CBOE', 'CDW', 'SCHW', 'CHTR', 'CSCO', 'CTXS', 
'CLX', 'KO', 'CMCSA', 'COST', 'CVS', 'DVN', 'DISH', 'DPZ', 'DOW', 'ETFC'] 

# axed symbols: CFPZF ARDS CHPRF CRPB GELYF TCNNF TDS PROSY GOPRO TWTR