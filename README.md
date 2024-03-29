# dYdX Algorithmic Trading Bot

## Disclaimer

This project is educational purpose only, the algorithm might bring losses. Use it at your own risk.

## Prepare env variables

```bash
INFURA_PROJECT_ID=
ETH_ADDRESS=
# get stark key pair and api credentials from the browser console(Application Tab -> Local Storage) when you login the to dashboard
STARK_PRIVATE_KEY=
API_KEY=
API_PASSPHRASE=
API_SECRET=
# pass the eth address to the get_account request, you will get the positionId back
POSITION_ID=
```

## Install deps

```bash
make install
```

## Run it

```bash
make run
```

## Available requests on dYdX

```python
markets_response = client.public.get_markets()
pprint(markets_response.data['markets'][MARKET_ADA_USD])

candles_response = client.public.get_candles(
    market=MARKET_ADA_USD,
    resolution='30MINS'
)
pprint(candles_response.data)

account_response = client.private.get_account(
    ethereum_address='0x3fe444...'
)
pprint(account_response.data)

orders_response = client.private.get_orders(
    market=MARKET_ADA_USD,
    status=ORDER_STATUS_OPEN
)
pprint(orders_response.data)

api_keys_response = client.private.get_api_keys()
pprint(api_keys_response.data)

positions_response = client.private.get_positions(
    market=MARKET_ADA_USD,
    status=POSITION_STATUS_OPEN,
)
pprint(positions_response.data)
```

## LICENSE
MIT

Created by [crazyoptimist](https://github.com/crazyopimist)
