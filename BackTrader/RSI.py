from datetime import datetime
import backtrader as bt
import yfinance as yf
from matplotlib import warnings
from matplotlib.dates import (HOURS_PER_DAY, MIN_PER_HOUR, SEC_PER_MIN,
    MONTHS_PER_YEAR, DAYS_PER_WEEK, SEC_PER_HOUR,
    SEC_PER_DAY, num2date, rrulewrapper,
    YearLocator, MicrosecondLocator)


class MyStrategy(bt.Strategy):  
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close)  
    def next(self):  
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()
        else:
            if self.rsi > 70:
                self.order = self.sell()

cerebro = bt.Cerebro()  
cerebro.addstrategy(MyStrategy)
data = bt.feeds.PandasData(dataname=yf.download('036570.KS', '2017-06-01', '2021-10-09', auto_adjust=True))
cerebro.adddata(data)
cerebro.broker.setcash(10000000) 
cerebro.addsizer(bt.sizers.SizerFix, stake=30)  

print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.run()  
print(f'Final Portfolio Value   : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.plot() 
