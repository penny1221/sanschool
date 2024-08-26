# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup;
import requests

url = "https://news.cts.com.tw/real/index.html";

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',

    'Cookie':'_gid=GA1.3.785965807.1723114620; AviviD_uuid=8a563826-b74f-43f8-9e4b-1314a3ed0779; webuserid=d02e626d-7f44-4cb1-acaa-202b259f10c0; _fbp=fb.2.1723114620741.53939273747123151; ch_tracking_uuid=1; __htid=b4ed551d-b362-4a12-b7a7-4ec7800022dd; _ht_em=1; _ht_47b240=1; ISMD5VERSION=1; CFFPCKUUID=9862-SNCj4JanUIc8mgwQFPaIO1qNtSYBevMk; CFFPCKUUIDMAIN=953-9MhG3E3UdDfn2NQpt3IMiCU4G7JIXFUB; FPUUID=0953-8502ebd2c6161ffb3a9b1f1abc9e7a8e; _ht_hi=1; _ht_50ef57=1; AWSALB=EGpnYghF6OqgoT6bPp5z8gliTA2K2rluHDzrSv0FZPBheykGT91oo1C8l2+G3VRl9LwO9dRyhy+Wm/zWfAcJIP42ERyNRuMGffAi3OJa6kV9gXfXwKJiFiopXfAr; AWSALBCORS=EGpnYghF6OqgoT6bPp5z8gliTA2K2rluHDzrSv0FZPBheykGT91oo1C8l2+G3VRl9LwO9dRyhy+Wm/zWfAcJIP42ERyNRuMGffAi3OJa6kV9gXfXwKJiFiopXfAr; AviviD_refresh_uuid_status=2; __gads=ID=0469b48e7b2c4eee:T=1723114621:RT=1723114957:S=ALNI_Mbhxzz6t7AZmf_fUDuVAMLBLt6qgA; __gpi=UID=00000eb92cf87e67:T=1723114621:RT=1723114957:S=ALNI_MZQ9Mfx1JvjeCOVaxkbnbzo6Kcy6w; __eoi=ID=6de5c96e054749cd:T=1723114621:RT=1723114957:S=AA-AfjbSUVr9Os5qLTAMI4Jfmw2R; _ga=GA1.3.1644068146.1723114620; _ga_FWQF4JLMB1=GS1.3.1723114620.1.1.1723114979.39.0.0; _ga_F6LZM62QYC=GS1.3.1723114620.1.1.1723114979.38.0.0; _ga_B5S0TX9D32=GS1.1.1723114620.1.1.1723114980.36.0.1977600592; FCNEC=%5B%5B%22AKsRol-qJEe-bsZrq210JwCQDIIN6tEJnBbuU8bnsa6rFYNaDtjhsU-tC6yV6I9Y7WBRoLRCc6vLotJrGeS5xIDRKyIwNPxGXstWuPNfNAohq57BxFn3df-54di-IIFrM4GQpJqjI-jrn1Ph8_ZgSjfz-26MyK5xYA%3D%3D%22%5D%5D'
    }

data = requests.get(url,headers = header);
data.encoding = "utf-8";
data = data.text;
#通常到此要進行確認是否有東西可以爬
#print(data);

soup = BeautifulSoup(data,'html.parser');

allnews = soup.find(id="newslist-top");
news = allnews.find_all('a');

for row in news:
    #print(row);    
    link = row.get('href');
    title = row.get('title');
    
    h3 = row.find('h3');
    
    if (h3 != None):
        h3 = h3.text.strip();
        
    else:
        h3 = 'none';
    
    img = row.find('img')
    
    if (img != None):
        photo = img.get('data-src');
        
        if photo == None:
            photo = img.get('src');
    
    else:
        photo = 'none';
        
    
    print("標題",title);
    print("連結",link);
    print("h3",h3);
    print("圖片",photo);
    print();
    