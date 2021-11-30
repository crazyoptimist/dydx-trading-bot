import os
import time
from dotenv import load_dotenv
from dydx3 import Client
from dydx3.constants import API_HOST_MAINNET, NETWORK_ID_MAINNET, \
        ORDER_SIDE_BUY, ORDER_SIDE_SELL, ORDER_TYPE_MARKET, ORDER_STATUS_OPEN, \
        POSITION_STATUS_OPEN, POSITION_STATUS_CLOSED, \
        MARKET_BTC_USD, MARKET_ETH_USD, MARKET_AVAX_USD, MARKET_ADA_USD
from web3 import Web3
from pprint import pprint
import pandas as pd
import numpy as np


load_dotenv()
WEB3_PROVIDER_URL = 'https://mainnet.infura.io/v3/' + os.getenv('INFURA_PROJECT_ID')


client = Client(
    network_id=NETWORK_ID_MAINNET,
    host=API_HOST_MAINNET,
    eth_private_key=os.getenv('ETH_PRIVATE_KEY'),
    web3=Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))
)

# markets_response = client.public.get_markets()
# pprint(markets_response.data['markets'][MARKET_ADA_USD])

# candles_response = client.public.get_candles(
#     market=MARKET_ADA_USD,
#     resolution='30MINS'
# )
# pprint(candles_response.data)

# account_response = client.private.get_account()
# pprint(account_response.data)

# orders_response = client.private.get_orders(
#     market=MARKET_ADA_USD,
#     status=ORDER_STATUS_OPEN
# )
# pprint(orders_response.data)

# api_keys_response = client.private.get_api_keys()
# pprint(api_keys_response.data)

# positions_response = client.private.get_positions(
#     market=MARKET_ADA_USD,
#     status=POSITION_STATUS_OPEN,
# )
# pprint(positions_response.data)

class DydxData:
    def __init__(self):
        candles_response = client.public.get_candles(
            market=MARKET_ADA_USD,
            resolution='5MINS',
            limit=10
        )
        self.data = candles_response.data['candles']
        self.df = pd.DataFrame(self.data)
        self.df['close'] = self.df['close'].astype(float)

    def find_z(self):
        mean = self.df['close'].mean()
        std = np.std(self.df['close'])
        z_score = (self.df['close'].iloc[0] - mean)/std
        print(z_score)


dydx_data = DydxData()
dydx_data.find_z()
