#!/usr/bin/python

""".
Queries the macaddress.io api for vendor information.
Example:
        ~$ python mac_utils.py  $MAC_ADDRESS  $API_TOKEN

"""

import requests
import sys
macaddress=sys.argv[1]
token=sys.argv[2]
print(macaddress)
url = 'https://api.macaddress.io/v1?apiKey=%s&output=json&search=%s' % (token, macaddress)
s = requests.get(url)
r = s.json()
name = r['vendorDetails']['companyName']
print "Company Name is:" ,name
