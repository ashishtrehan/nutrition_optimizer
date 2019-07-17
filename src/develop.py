import requests
import json
import parameters
import os
from urllib.parse import urlencode, quote_plus
from util import unpack


api_key = os.environ['API_KEY']

class Search(object):
    def __init__(self,data):
        self.usda = data.get('list')
        self.items = self.usda.get('item')

class List(object):
    def __init__(self,data):
        self.keys = data.keys()
        self.sr = data.get('sr')
        self.sort = data.get('sort')
        self.end = data.get('end')
        self.item = data.get('item')
        self.start = data.get('start')
        self.group = data.get('group')
        self.ds = data.get('ds')
        self.total = data.get('total')
        self.q = data.get('q')

class Item(object):
    def __init__(self,data):
        self.offset = 0



class USDA():
    def __init__(self):
        self.food = 'mozzarella'
        self.amount =  'grams'
        self.usda_api = api_key
        self.values = {'format': 'json', 'q': self.food, 'sort': 'n', 'max' : '100','offset': '0', 'api_key': self.usda_api}

    def first_search(self):
        data = urlencode(self.values)
        url = 'http://api.nal.usda.gov/usda/ndb/search/?' + str(data)
        r = requests.get(url=url)
        data = json.loads(r.text)
        return List(Search(data).usda).item


a = (USDA().first_search())
print (a)
