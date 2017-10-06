#!/usr/bin/python3.5

"""

Just, at the moment, a simple attempt to return some data from bittrex.com crypto-exchange

Goal=to create the "Cadillac" of FOSS cryptocurrency trading bots. No, seriously, lol!

written by prometx@gmail.com 9-23-17

"""


from bittrex import Bittrex
import sys
import time
import json
import requests
import urllib3
from pprint import pprint


"""

So, here is where you will enter your API key-pair (key and secret)
to communicate with the Bittrex exchange. NOTE: bittrex.py

"""

# declare your API Key and Key Secret, these are, of course, SECRETS
# if I've been an idiot and left my keys in here, for a "public" version of this file
#please do me a solid and remove them and notify me at prometx@gmail.com ;), thanks...

api_key = '<bittrex api key>'
api_secret = '<bittrex api secret>'

"""

PUBLIC_SET = {
	
	'getmarkets',
	'getcurrencies',
	'getticker',
	'getmarketsummaries'
	'getmarketsummary'
	'getorderbook'
	'getmarkethistory'	

MARKET_SET = {

    'getopenorders',
    'cancel',
    'sellmarket',
    'selllimit',
    'buymarket',
    'buylimit'

}

ACCOUNT_SET = {

    'getbalances',
    'getbalance',
    'getdepositaddress',
    'withdraw',
    'getorderhistory',
    'getorder',
    'getdeposithistory',
    'getwithdrawalhistory'

}

"""

method_set = 'market'
method = 'getopenorders'
call = Bittrex(api_key,api_secret)

#BASE_URL = 'https://bittrex.com/api/v1.1/{method_set}/{method}?'

api_url = 'https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-xmr'


"""
if method in MARKET_SET:
	method_set = 'market'
elif method in ACCOUNT_SET:
	method_set = 'account'
"""

def main(argv):

	r = requests.get(api_url)

	r.json()

	print(r.json())

	print(\n * 4)

	pprint.pprint(r.json())

	print(\n * 4)

if __name__ == "__main__":
	main(sys.argv[1:])



