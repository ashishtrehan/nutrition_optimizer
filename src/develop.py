import requests
import json
import parameters
import os
from urllib.parse import urlencode, quote_plus


api_key = os.environ['API_KEY']

class USDA():
    def __init__(self):
        self.food = input('Enter a food')
        self.amount =  input('grams? oz? cup? Tbl spoon')
        self.usda_api = api_key
        self.values = {'format': 'json', 'q': self.food, 'sort': 'n', 'max' : '100','offset': '0', 'api_key': self.usda_api}

    def first_search(self):
        data = urlencode(self.values)
        url = 'http://api.nal.usda.gov/usda/ndb/search/?' + str(data)
        print (url)
        r = requests.get(url=url)
        print (r.text)
        return r.text


USDA().first_search()
