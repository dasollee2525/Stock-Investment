class NasdaqStock:
  """Class for NASDAQ stocks"""
  count = 0
  def __init__(self, symbol, price):
    """Constructor for NasdaqStock"""
    self.symbol = symbol
    self.price = price
    NasdaqStock.count += 1
    print("Calling __init__({}, {:.2f}) > count: {}'.format
         (self.symbol, self.price, NasdaqStock.count))
    
  def __del__(self):
    """Destructor for NasdaqStock"""
    print('Calling__del__({})'.format(self))
    

google = NasdaqStock("GOOG', 111.83)
del(google)
amazon = NasdaqStock("AMZN', 115.69)
del(amazon)                 
