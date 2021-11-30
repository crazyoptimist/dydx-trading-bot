# dYdX Sniper Bot

## Install Deps
```bash
make install
```

## Run It
```bash
make run
```

## Available Requests on dYdX
```python
markets_response = client.public.get_markets()
pprint(markets_response.data['markets'][MARKET_ADA_USD])

candles_response = client.public.get_candles(
    market=MARKET_ADA_USD,
    resolution='30MINS'
)
pprint(candles_response.data)

account_response = client.private.get_account()
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
Top secret! LOL

Created by [CrazyOptimist](https://github.com/crazyopimist)
