from django.shortcuts import render
from bs4 import BeautifulSoup 
import requests

def get_data(symbol):
    url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(symbol)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    bs = BeautifulSoup(html, 'lxml')
    cur_price = bs.find('strong', id='_nowVal')  
    cur_rate = bs.find('strong', id='_rate')  
    stock = bs.find('title') 
    stock_name = stock.text.split(':')[0].strip()  
    return cur_price.text, cur_rate.text.strip(), stock_name
            

def main_view(request):
    querydict = request.GET.copy()
    mylist = querydict.lists()  
    rows = []
    total = 0

    for x in mylist:
        cur_price, cur_rate, stock_name = get_data(x[0])       
        price = cur_price.replace(',', '')
        stock_count = format(int(x[1][0]), ',')  
        sum = int(price) * int(x[1][0])
        stock_sum = format(sum, ',')         
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate,
            stock_sum])  
        total = total + int(price) * int(x[1][0])  

    total_amount = format(total, ',')       
    values = {'rows' : rows, 'total' : total_amount}  
    return render(request, 'balance.html', values)  