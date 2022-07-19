import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
from scipy import stats
import matplotlib.pylab as plt

dow = pdr.get_data_yahoo("^DJI", '2000-01-04')
kospi = pdr.get_data_yahoo("^KS11", '2000-01-04')
us_treasury = pdr.get_data_yahoo("TLT", '2000-01-04')

df1 = pd.DataFrame({'X': dow['Close'], 'Y': kospi['Close']})
df1 = df1.fillna(method='bfill')
df1 = df1.fillna(method='ffill')

regr1 = stats.linregress(df1.X, df1.Y)
regr_line1 = f'Y = {regr1.slope:.2f} * X + {regr1.intercept:.2f}'


df2 = pd.DataFrame({'X': us_treasury['Close'], 'Y': kospi['Close']})
df2 = df2.fillna(method='bfill')
df2 = df2.fillna(method='ffill')

regr2 = stats.linregress(df2.X, df2.Y)
regr_line2 = f'Y = {regr2.slope:.2f} * X + {regr2.intercept:.2f}'

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.plot(df1.X, df1.Y, '.')
plt.plot(df1.X, regr1.slope * df1.X + regr1.intercept, 'r')
plt.legend(['DOW x KOSPI', regr_line1])
plt.title(f'DOW x KOSPI (R = {regr1.rvalue:.2f})')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')

plt.subplot(122)
plt.plot(df2.X, df2.Y, 'x', c='g')
plt.plot(df2.X, regr2.slope * df2.X + regr2.intercept, 'r')
plt.legend(['US_Treasury x KOSPI', regr_line2])
plt.title(f'US_Treasury x KOSPI (R = {regr2.rvalue:.2f})')
plt.xlabel('iShares 20 + Year Treasury Bond ETF')
plt.ylabel('KOSPI')
plt.show()