import os
import time
from dotenv import load_dotenv
from dydx3 import Client
from dydx3.constants import API_HOST_MAINNET, NETWORK_ID_MAINNET, \
        ORDER_SIDE_BUY, ORDER_SIDE_SELL, \
        ORDER_TYPE_MARKET, ORDER_TYPE_STOP, ORDER_TYPE_TRAILING_STOP, ORDER_TYPE_TAKE_PROFIT, \
        ORDER_STATUS_OPEN, ORDER_STATUS_PENDING, ORDER_STATUS_FILLED, ORDER_STATUS_UNTRIGGERED, \
        POSITION_STATUS_OPEN, POSITION_STATUS_CLOSED, \
        MARKET_BTC_USD, MARKET_ETH_USD, MARKET_AVAX_USD, MARKET_ADA_USD, MARKET_ALGO_USD
from web3 import Web3
import pandas as pd
import numpy as np
from pprint import pprint


load_dotenv()
WEB3_PROVIDER_URL = 'https://mainnet.infura.io/v3/' + os.getenv('INFURA_PROJECT_ID')
DEVIATION_THRESHOLD = 0.3 # multiply of standard deviation
TARGET_MARKET = MARKET_ADA_USD
ORDER_SIZE = '10'
ORDER_TYPE = ORDER_TYPE_TRAILING_STOP
TRAILING_PERCENT = 1


client = Client(
    network_id=NETWORK_ID_MAINNET,
    host=API_HOST_MAINNET,
    eth_private_key=os.getenv('ETH_PRIVATE_KEY'),
    web3=Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL)),
    stark_private_key=os.getenv('STARK_PRIVATE_KEY')
)


class DydxData:
    def __init__(self):
        candles_response = client.public.get_candles(
            market=TARGET_MARKET,
            resolution='5MINS',
            limit=10
        )
        self.data = candles_response.data['candles']
        self.df = pd.DataFrame(self.data)
        self.df['close'] = self.df['close'].astype(float)
        print(self.df['startedAt'].iloc[0])

    def find_z(self):
        mean = self.df['close'].mean()
        std = np.std(self.df['close'])
        z_score = (self.df['close'].iloc[0] - mean)/std
        return z_score


def place_order(order_params):
    order_creation_response = client.private.create_order(**order_params)
    print(order_creation_response)


def job():
    dydx_data = DydxData()
    z_score = dydx_data.find_z()
    order_params = {
        'position_id': 1,
        'market': TARGET_MARKET,
        'order_type': ORDER_TYPE,
        'post_only': True,
        'size': ORDER_SIZE,
        'price': str(dydx_data.df['close'].iloc[0]),
        'limit_fee': 0.001,
        'expiration_epoch_seconds': 2419200,
    }
    if not (z_score > DEVIATION_THRESHOLD or z_score < -DEVIATION_THRESHOLD):
        print("Deviation does not exceed the limit")
        return
    elif z_score > DEVIATION_THRESHOLD:
        order_params = {
            **order_params,
            'side': ORDER_SIDE_BUY,
            'trailing_percent': TRAILING_PERCENT
        }
        place_order(order_params)
        return
    elif z_score < -DEVIATION_THRESHOLD:
        order_params = {
            **order_params,
            'side': ORDER_SIDE_SELL,
            'trailing_percent': -TRAILING_PERCENT
        }
        place_order(order_params)
        return

    orders_response = client.private.get_orders(
        market=TARGET_MARKET,
        status=ORDER_STATUS_UNTRIGGERED
    )
    pprint(orders_response.data)

