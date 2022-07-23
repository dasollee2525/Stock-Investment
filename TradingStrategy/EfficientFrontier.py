import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import MarketPriceAPI

mk = MarketPriceAPI.MarketDB()
#stocks = ['Samsung Electronics', 'SK Hynix', 'Samsung Biologics', 'NAVER']
#이름으로도 조회할 수 있게 개선이 필요
stocks = ['005930', '000660', '207940', '035420']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.getDailyPrice(s, '2018-10-15', '2022-07-23')['close']

df.columns = ['Samsung Electronics', 'SK Hynix', 'Samsung Biologics', 'NAVER']

"daily fluctuation rate"
daily_ret = df.pct_change()
print(daily_ret)
"annual mean flutation rate"
annual_ret = daily_ret.mean() * 247
"covariance"
daily_cov = daily_ret.cov()
"annual covariance"
annual_cov = daily_cov * 247

port_ret = [] 
port_risk = [] 
port_weights = [] 
#create 10,000 numbers of portfolio
for _ in range(50000): 
    weights = np.random.random(len(stocks)) 
    weights /= np.sum(weights) 

    returns = np.dot(weights, annual_ret) 
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights))) 

    port_ret.append(returns) 
    port_risk.append(risk) 
    port_weights.append(weights) 

portfolio = {'Returns': port_ret, 'Risk': port_risk} 
for i, s in enumerate(stocks): 
    portfolio[s] = [weight[i] for weight in port_weights] 
df = pd.DataFrame(portfolio) 
df = df[['Returns', 'Risk'] + [s for s in stocks]] 

df.plot.scatter(x='Risk', y='Returns', figsize=(8, 6), grid=True)
plt.title('Efficient Frontier') 
plt.xlabel('Risk') 
plt.ylabel('Expected Returns') 
plt.show() 
