import requests
import time
from PaperConfig import * #contains api keys

BASE_URL = "https://paper-api.alpaca.markets" #the main endpoint for requests
ACCOUNT_URL = "{}/v2/account".format(BASE_URL) #endpoint for account details

#get request for account data associated with API keys in PaperConfig
r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}) 

#prints out the content of r
print(r.content)