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
sharpe_ratio = []

#create 10,000 numbers of portfolio
for _ in range(50000): 
    weights = np.random.random(len(stocks)) 
    weights /= np.sum(weights) 

    returns = np.dot(weights, annual_ret) 
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights))) 

    port_ret.append(returns) 
    port_risk.append(risk) 
    port_weights.append(weights) 
    "측정된 위험 단위당 수익이 제일 높은 포트폴리오를 구하는 과정"
    sharpe_ratio.append(returns/risk)

portfolio = {'Returns': port_ret, 'Risk': port_risk, 'Sharpe': sharpe_ratio}
for i, s in enumerate(stocks): 
    portfolio[s] = [weight[i] for weight in port_weights] 
df = pd.DataFrame(portfolio) 
df = df[['Returns', 'Risk', 'Sharpe'] + [s for s in stocks]]  

max_sharpe = df.loc[df['Sharpe'] == df['Sharpe'].max()]  
min_risk = df.loc[df['Risk'] == df['Risk'].min()]  

df.plot.scatter(x='Risk', y='Returns', c='Sharpe', cmap='viridis',
    edgecolors='k', figsize=(11,7), grid=True) 
plt.scatter(x=max_sharpe['Risk'], y=max_sharpe['Returns'], c='r', 
    marker='*', s=300)
plt.text(max_sharpe['Risk']+0.0075, max_sharpe['Returns'], np.round(max_sharpe.iloc[:, 3:7].values.tolist()[0], 3), 
    c="w", backgroundcolor="r") 
plt.scatter(x=min_risk['Risk'], y=min_risk['Returns'], c='r', 
    marker='o', s=200)  
plt.text(min_risk['Risk']+0.0075, min_risk['Returns'], np.round(min_risk.iloc[:, 3:7].values.tolist()[0], 3), 
    c="w", backgroundcolor="r") 
plt.title('Portfolio Optimization') 
plt.xlabel('Risk') 
plt.ylabel('Expected Returns') 
plt.show()
