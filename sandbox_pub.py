import urllib3
import requests
import pprint

api_url = 'https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-xmr'

r = requests.get(api_url)

r.json()

print(r.json())

pprint.pprint(r.json())

		

