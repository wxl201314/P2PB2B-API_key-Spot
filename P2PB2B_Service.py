from P2PB2BEX.p2pb2b_api import Api


key = ''
secret = ''
p2p_api = Api(key,secret)
class P2PB2B_API:
	
	#获取最新价
	def get_last_price(self,symbol):
		
		data = p2p_api.public.ticker(market=symbol)
		if data.get('success') == True:
			return float(data.get('result').get('last'))
		else:
			return None
		
	#获取K线数据
	def get_kline_data(self,symbol,interval,offset=0,limit=100):
		
		data = p2p_api.public.market.kline(market=symbol,interval=interval,offset=offset,limit=limit)
		"""
		m -> minutes; h -> hours; d -> days;
		interval:1m,1h,1d...
		"""
		return data
		
	#获取账户某币种可用余额
	def get_balance(self,base):
		data = p2p_api.account.balance(currency = base)
		if data.get('success') == True:
			return float(data.get('result').get('available'))
		else:
			return None
	
	#获取深度
	def get_depth(self,symbol):

		data = p2p_api.public.depth.result(market = symbol)
		if data.get('success') == True:
			return data.get('result')
		else:
			return None
	
	#获取未成交订单
	def get_executed_history(self,symbol):
		data = p2p_api.account.executed_history(market=symbol)
		if data.get('success') == True:
			return data.get('result')
		else:
			return None
	
	#创建订单
	def create_order(self,symbol,price,amount,side):
		data = p2p_api.order.new(market = symbol,price = price,amount = amount,side = side)
		return data
	
	#取消订单
	def cancel_order(self,symbol,orderid):
		data = p2p_api.order.cancel(market = symbol,orderId = orderid)
		return data
	
	#取消所有订单
	def cancel_all_orders(self,symbol):
		data = p2p_api.order.cancel.all(market=symbol)
		if data.get('success') == True:
			print('全部撤单成功')
		else:
			print('全部撤单失败')
	
	#获取订单成交历史
	def get_order_history(self):
		return p2p_api.account.order_history()

if __name__ == "__main__":
	q = P2PB2B_API()
	print(q.get_kline_data('BTC_USDT','1m'))
