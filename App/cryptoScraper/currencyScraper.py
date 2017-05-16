import time
from datetime import datetime
import requests
from db.sqlite_init import add

#############################################
############       Okcoin       #############
#############################################

class okcoin_btc_usd:

    def __init__(self):
        self.name = 'okcoin_btc_usd'
        #self.collection = okcoin_btc_usd_Collection
        self.ticker = requests.get('https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd').json()
        self.depth = requests.get('https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd&size=60').json()
        self.timestamp = int(self.ticker['date'])
        self.price = float(self.ticker['ticker']['last'])
        self.v_bid = round(sum([bid[1] for bid in self.depth['bids']]), 3)
        self.v_ask = round(sum([ask[1] for ask in self.depth['asks']]), 3)

        #print(self.name,self.timestamp, self.price, self.v_bid, self.v_ask)
        add(self.name,self.timestamp, self.price, self.v_bid, self.v_ask)
        #add(self.collection, self.timestamp, self.price, self.v_bid, self.v_ask)
        
class okcoin_ltc_usd:

    def __init__(self):
        self.name = 'okcoin_ltc_usd'
        #self.collection = okcoin_btc_usd_Collection
        self.ticker = requests.get('https://www.okcoin.com/api/v1/ticker.do?symbol=ltc_usd').json()
        self.depth = requests.get('https://www.okcoin.com/api/v1/depth.do?symbol=ltc_usd&size=60').json()
        self.timestamp = int(self.ticker['date'])
        self.price = float(self.ticker['ticker']['last'])
        self.v_bid = round(sum([bid[1] for bid in self.depth['bids']]), 3)
        self.v_ask = round(sum([ask[1] for ask in self.depth['asks']]), 3)

        #print(self.name,self.timestamp, self.price, self.v_bid, self.v_ask)
        add(self.name,self.timestamp, self.price, self.v_bid, self.v_ask)
        #add(self.collection, self.timestamp, self.price, self.v_bid, self.v_ask)

