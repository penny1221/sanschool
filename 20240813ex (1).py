# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:11:17 2024

@author: USER
"""

import requests;
import json;

url = "https://www.thsrc.com.tw/TimeTable/Search";

header = {
    
    'Cookie':'_ga_1FDVRGS3MR=GS1.1.1723550357.1.0.1723550357.60.0.0; _gcl_au=1.1.652045268.1723550358; _td_cid=1264487614.1723550358; _fbp=fb.2.1723550358608.10182372991362704; _ga=GA1.3.1420379243.1723550358; _gid=GA1.3.1404698785.1723550359; AcceptThsrcCookiePolicyTime=Tue%20Aug%2013%202024%2020:00:31%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93); _ga_6M07CCJT7N=GS1.1.1723550358.1.1.1723551111.60.0.0',

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    
    }

params = {
    
    'SearchType': 'S',
    'Lang': 'TW',
    'StartStation': 'NanGang',
    'EndStation':'ZuoYing',
    'OutWardSearchDate': '2024/08/13',
    'OutWardSearchTime': '20:00',
    'ReturnSearchDate': '2024/08/13',
    'ReturnSearchTime': '20:00',
    'DiscountType': ''
    
    }

data = requests.post(url,headers = header,data = params).text;

#print(data);

thsrc = json.loads(data);

thsrc = thsrc['data']['DepartureTable']['TrainItem'];

for row in thsrc:
    print('車次:',row['TrainNumber']);
    print('出發時間:',row['DepartureTime']);
    print('旅行時間:',row['Duration']);
    print('抵達時間:',row['DestinationTime']);
    
    station = [];
    for s in row['StationInfo']:
        if s['Show']:
            station.append(s['StationName']);
    
    print('停靠站:',station);
    
    print();