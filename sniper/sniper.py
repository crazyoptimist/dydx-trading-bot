import os
import time
from dotenv import load_dotenv
from dydx3 import Client
from dydx3.constants import API_HOST_MAINNET, NETWORK_ID_MAINNET, \
        ORDER_SIDE_BUY, ORDER_SIDE_SELL, ORDER_TYPE_MARKET, ORDER_STATUS_OPEN, \
        POSITION_STATUS_OPEN, POSITION_STATUS_CLOSED, \
        MARKET_BTC_USD, MARKET_ETH_USD, MARKET_AVAX_USD, MARKET_ADA_USD
from web3 import Web3


load_dotenv()
WEB3_PROVIDER_URL = 'https://mainnet.infura.io/v3/' + os.getenv('INFURA_PROJECT_ID')


client = Client(
    network_id=NETWORK_ID_MAINNET,
    host=API_HOST_MAINNET,
    eth_private_key=os.getenv('ETH_PRIVATE_KEY'),
    web3=Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))
)

account_response = client.public.get_markets()
print(account_response.data)
