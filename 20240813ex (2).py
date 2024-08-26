# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup;
import  requests;

url = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation";

header = {
    
    'Cookie':'_ga=GA1.1.80927525.1723546401; _ga_9P3LQ5F3SZ=GS1.1.1723546400.1.1.1723547014.0.0.0',

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    
    }

#參數
params = {
   
   ' _csrf': '66f74619-063c-4df3-8fa3-75cf76e43b9a',
   'rideDate': '2024/08/13',
   'station': '3300-臺中'
    
   }

data = requests.post(url,headers = header,data = params);

data.encoding = "utf-8";

data = data.text;

soup = BeautifulSoup(data,'html.parser');

tab1 = soup.find(id = 'tab1');
tab2 = soup.find(id = 'tab2');

tabtr = tab1.find_all('tr');

for row in tabtr:
    tds = row.find_all('td');
    
    if( len(tds) > 0 ):
        print('車種車次 (始發站 → 終點站):',tds[0].text.strip().replace("\n",""));
        print('出發時間:',tds[1].text.strip());
        print('終點站:',tds[2].text.strip());
        print('服務設施:',tds[3].text.strip());
        print('狀態:',tds[4].text.strip());
        print();


tabtr = tab2.find_all('tr');

for row in tabtr:
    tds = row.find_all('td');
    
    if( len(tds) > 0 ):
        print('車種車次 (始發站 → 終點站):',tds[0].text.strip().replace("\n",""));
        print('出發時間:',tds[1].text.strip());
        print('終點站:',tds[2].text.strip());
        print('服務設施:',tds[3].text.strip());
        print('狀態:',tds[4].text.strip());
        print();