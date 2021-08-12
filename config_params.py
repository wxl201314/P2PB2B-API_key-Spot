#############################################################
# author : Yaozhang
# email : 1125564921@qq.com
#############################################################

# base url
P2P_Base_URL = 'https://p2pb2b.io'
KEY = 'bde29aece568c883440467704f905aaf'
secretKey = '04d0fb31152555a7d34a26b906e14a49'

# Get info on all markets.
# curl --location --request GET "http://api.p2pb2b.io/api/v2/public/markets"
MARKET_INFO_LIST_API = P2P_Base_URL + "/api/v2/public/markets"

# Get info by market.
# curl --location --request GET "http://api.p2pb2b.io/api/v2/public/market?market=ETH_BTC"
MARKET_INFO_ONE_API = P2P_Base_URL + "/api/v2/public/market?market={market}"

# Get trade details for all tickers.
# curl --location --request GET "http://api.p2pb2b.io/api/v2/public/tickers"
TICKERS_INFO_LIST_API = P2P_Base_URL + "/api/v2/public/tickers"

# Get trade details for a ticker.
# curl --location --request GET "http://api.p2pb2b.io/api/v2/public/ticker?market=ETH_BTC"
TICKER_INFO_ONE_API = P2P_Base_URL + '/api/v2/public/ticker?market={market}'

# Get all unexecuted orders by market.
# curl --location --request GET "https://api.p2pb2b.io/api/v2/public/book?market=ETH_BTC&side=sell&offset=0&limit=100"
BOOK_UNEXECUTED_ORDERS_API = P2P_Base_URL + '/api/v1/public/book?market={market}&side={side}&offset={offset}&limit={limit}'

# Each order history starts with order ID.
# curl --location --request GET "https://api.p2pb2b.io/api/v2/public/history?market=ETH_BTC&lastId=1&limit=100"
HISTORY_ORDER_ID_API = P2P_Base_URL + '/api/v2/public/history?market={market}&lastId={lastId}&limit={limit}'

# Order depth for a market.
# curl --location --request GET "https://api.p2pb2b.io/api/v2/public/depth/result?market=ETH_BTC&limit=100"
DEPTH_MARKET_API = P2P_Base_URL + '/api/v2/public/depth/result?market={market}&limit={limit}'

# Kline/candlestick bars for a market. Kline identification takes place at the opening time.
# curl --location --request GET "http://api.p2pb2b.io/api/v2/public/market/kline?market=ETH_BTC&interval=1m&offset=0&limit=100"
KLINE_MARKET_BARS_API = P2P_Base_URL + '/api/v2/public/market/kline?market={market}&interval={interval}&offset={offset}&limit={limit}'


# ------------------------------------------------------------------------------------------------------------


# A request to a private API must have a set of required headers, with which the user is authenticated.

# List of user balances for all currencies.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/account/balances"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"request":"{{request}}","nonce":"{{nonce}}"}"
"""
GET_ALL_CURRENCIES_BALANCES_API = P2P_Base_URL + '/api/v2/account/balances'

# User balance for the selected currency.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/account/balance"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"currency":"ETH","request":"{{request}}","nonce":"{{nonce}}"}"

"""
GET_SELECTED_CURRENCY_API = P2P_Base_URL + '/api/v2/account/balance'

# Query executed orders.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/account/order_history"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"request":"{{request}}","nonce":"{{nonce}}"}"
"""
QUERY_EXECUTED_ORDERS_API = P2P_Base_URL + '/api/v2/account/order_history"'

# Query deal details by executed order ID.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/account/order"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"orderId":"123456","limit":"50","offset":"0","request":"{{request}}","nonce":"{{nonce}}"}"
"""
QUERY_EXECUTED_ORDER_DETAILS_API = P2P_Base_URL + '/api/v2/account/order'

# List of executed user orders for a market.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/account/executed_history"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"market":"ETH_BTC","limit":"1","offset":"0","request":"{{request}}","nonce":"{{nonce}}"}"
"""
USER_EXECUTED_ORDERS_MARKET_API = P2P_Base_URL + '/api/v2/account/executed_history'

# List of executed user orders for all markets.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/account/executed_history/all"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"limit":"10","offset":"0","request":"{{request}}","nonce":"{{nonce}}"}"
"""
ALL_MARKETS_ORDERS_LIST_API = P2P_Base_URL + '/api/v2/account/executed_history/all'

# Query unexecuted orders.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/orders"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"market":"ETH_BTC","limit":"50","offset":"0","request":"{{request}}","nonce":"{{nonce}}"}"
"""
QUERY_UNEXECUTED_ORDERS_API = P2P_Base_URL + '/api/v1/orders'

# Сreating an order for a trade.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/order/new"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"market":"ETH_BTC","side":"buy","amount":"0.001","price":"0.001","request":"{{request}}","nonce":"{{nonce}}"}"
"""
CREATE_ORDER_TRADE_API = P2P_Base_URL + '/api/v2/order/new'

# Cancel an active order for a market by order ID.
"""
curl --location --request POST "https://api.p2pb2b.io/api/v2/order/cancel"
  --header "Content-Type: application/json" \
  --header "X-TXC-APIKEY: {{apiKey}}" \
  --header "X-TXC-PAYLOAD: {{payload}}" \
  --header "X-TXC-SIGNATURE: {{signature}}" \
  --data "{"market":"ETH_BTC", "orderId":"123456","request":"{{request}}","nonce":"{{nonce}}"}"
"""
CANCEL_ORDER_BY_ID_API = P2P_Base_URL + '/api/v2/order/cancel'
