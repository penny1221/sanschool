# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:26:40 2024

@author: USER
"""
import requests
from bs4 import BeautifulSoup

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW";

data = requests.get(url).text;
soup = BeautifulSoup(data,'html.parser');

table = soup.find('table');

# print(table);

rate = table.find('tbody');

trs = rate.find_all('tr');

for row in trs:
    tds = row.find_all('td');
    
    currency = tds[0].text.strip();
    money = currency.split();
    currency = money[0]+money[1];
    
    cashbuy = tds[1].text.strip();
    
    cashsell = tds[2].text.strip();
    
    spotbuy = tds[3].text.strip();
    
    spotshell = tds[4].text.strip();
    
    print(currency,cashbuy,cashsell,spotbuy,spotshell);