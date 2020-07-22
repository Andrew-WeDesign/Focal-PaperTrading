API_KEY = 'PK98BJ774ZY2YSKWCQ13'
SECRET_KEY = 'NftUjD260izfFI88Ep2SWkQYJoqH5VDpBpNQwwNE'

BASE_URL = 'https://paper-api.alpaca.markets' #the main endpoint for requests
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL) #endpoint for account details
ORDERS_URL = '{}/v2/orders'.format(BASE_URL) #endpoint for orders
BARS_URL = 'https://data.alpaca.markets/v1/bars'

HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY} #required for each request
