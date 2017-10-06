#!/usr/bin/python

"""

Just, at the moment, a simple attempt to return some data from bittrex.com crypto-exchange

Goal=to create the "Cadillac" of FOSS cryptocurrency trading bots. No, seriously, lol!

written by prometx@gmail.com 9-23-17

"""


from bittrex import Bittrex
import sys
import time
import json
import urllib2
import urlparse

"""

So, here is where you will enter your API key-pair (key and secret)
to communicate with the Bittrex exchange. NOTE: bittrex.py

"""

# declare your API Key and Key Secret, these are, of course, SECRETS
# if I've been an idiot and left my keys in here, for a "public" version of this file
#please do me a solid and remove them and notify me at prometx@gmail.com ;), thanks...

api_key = '<bittrex api key>'
api_secret = '<bittrex api secret>'

def main(argv):

    call = Bittrex(api_key,api_secret)

	url = urllib2.urlopen
    
	call.api_query('getbalances')

    

    print ((call.api_query('getbalances')))


if __name__ == "__main__":
    main(sys.argv[1:])



