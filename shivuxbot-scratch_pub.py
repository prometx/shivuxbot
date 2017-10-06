#!/usr/bin/python3.5

import requests
import urllib.request
import urllib.parse
import json
import pprint
from bittrex import Bittrex

"""
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

api_key = '<bittrex api key>'
api_secret = '<bittrex api secret>'

#url = 'https://bittrex.com/api/v1.1/account/getbalances'

bittrex = Bittrex(api_key,api_secret)

call_result = call.api_query('account','getopenbalances')

json_data = requests.get(call_result).json()





