from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')

window = 250
#KOSPI 마감장 기준으로 1년(거래일 기준) 기간 단위로 최고치 peak를 조회
peak = kospi['Adj Close'].rolling(window, min_periods=1).max()
#peak 대비 KOSPI 종가가 얼마나 하락했는지 계산
drawdown = kospi['Adj Close']/peak - 1.0
#drawdown(손실)에서 1년 기간 단위로 최저치를 계산
max_dd = drawdown.rolling(window, min_periods=1).min()

plt.figure(figsize=(9, 7))
plt.subplot(211) #2 rows and 1 column -> select 1st row
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212) #2 rows and 1 column -> select 2nd row
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()
