"""
Gather possible decimal point
"""

from pprint import pprint

import requests
import csv
import json

url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))

# pprint(json_data)

# pprint(json_data['data'])
# pprint(json_data['data'][-1])


seven_days_ago_price = json_data['data'][-7]['priceUsd']
print(f"Seven Days Ago Price : {seven_days_ago_price}")
today_price = json_data['data'][-1]['priceUsd']
print(f"Today Price : {today_price}")
