from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
sec_dpc = ((sec['Close'] / sec['Close'].shift(1)) - 1) * 100
sec_dpc[0] = 0
sec_dpc_cs = sec_dpc.cumsum()

sk = pdr.get_data_yahoo('000660.KS', start='2018-05-04')
sk_dpc = (sk['Close'] / sk['Close'].shift(1) - 1) * 100
sk_dpc[0] = 0
sk_dpc_cs = sk_dpc.cumsum()

import matplotlib.pyplot as plt

plt.plot(sec.index, sec_dpc_cs, 'b', label="Samsung Electronics")
plt.plot(sk.index, sk_dpc_cs, 'r--', label="SK Hynix")
plt.ylabel('Change %')
plt.xlabel('Date')
plt.grid(True)
plt.legend(loc='best')
plt.show()

