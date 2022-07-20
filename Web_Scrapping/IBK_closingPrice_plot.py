import pandas as pd
from bs4 import BeautifulSoup
import requests
#using request rather than urllib
from matplotlib import pyplot as plt

url = 'https://finance.naver.com/item/sise_day.naver?code=024110&page=1'
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
pgrr = bs.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.naver?code=024110'

for page in range(1, int(last_page)+1):
    url = '{}&page={}'.format(sise_url, page)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = pd.concat([df, pd.read_html(html, header=0)[0]])

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by='날짜')

plt.title('IBK (close)')
#rotate 90 degree of x label
plt.xticks(rotation=45)  
#co: represent point as cyan color & -: represent connecting points by solid line
plt.plot(df['날짜'], df['종가'], 'co-')
plt.grid(color='gray', linestyle='--')
plt.show()
