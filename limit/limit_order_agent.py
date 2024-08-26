class LimitOrderAgent:  
   def __init__(self):  
      self.orders = []  
  
   def add_order(self, buy_or_sell, product_id, amount, limit):  
      order = {  
        'buy_or_sell': buy_or_sell,  
        'product_id': product_id,  
        'amount': amount,  
        'limit': limit  
      }  
      self.orders.append(order)  
  
   def execute_orders(self, market_price):  
      for order in self.orders:  
        if (order['buy_or_sell'] == 'buy' and market_price <= order['limit']) or \  
          (order['buy_or_sell'] == 'ell' and market_price >= order['limit']):  
           print(f"Executing order: {order['buy_or_sell']} {order['amount']} shares of {order['product_id']} at ${market_price}")  
           # Add code to execute the trade here  
           self.orders.remove(order)  
  
# Example usage:  
agent = LimitOrderAgent()  
agent.add_order('buy', 'IBM', 1000, 100)  
agent.execute_orders(90)  # This will execute the order  
agent.execute_orders(110)  # This will not execute the order

