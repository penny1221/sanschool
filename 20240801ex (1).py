# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:52:02 2024

@author: USER
"""

import requests
import json

url = "https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=5520b915-09d8-40ec-816e-033bac6bb9f5"

param = {
    "api_key":"5520b915-09d8-40ec-816e-033bac6bb9f5"
    }

#data = requests.get(url).text
data = requests.get(url,params = param).text #參數寫法
print(data)

air = json.loads(data)
allair = air['records']
#print(allair);

for item in allair:
    print('地區：',item['county'])
    print('AQI：',item['aqi'])
    print('品質：',item['status'])
    print()
    