# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:23:17 2024

@author: USER
"""

from bs4 import BeautifulSoup;
import requests

url = "https://news.tvbs.com.tw/realtime";

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Cookie':'AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.2002585817.1723123429; _gat=1; cho_weather=%E8%87%BA%E5%8C%97%E5%B8%82; _ga_PT43NBSMZN=GS1.3.1723123429.1.0.1723123429.60.0.0; _fbp=fb.2.1723123429680.948498654622946987; _ga_B8E0BLEGRH=GS1.1.1723123429.1.0.1723123429.0.0.1749986852; _ga=GA1.1.2063140311.1723123429; _clck=1554b8b%7C2%7Cfo5%7C0%7C1681; FPID=FPID2.3.FTUBD7JSdpyo8RRAIEvZm%2FeDzw5tQmZmt1FnCI65So8%3D.1723123429; FPLC=o9r0rGC7EIkmS0ICj5KgGEgg3crsbPjTsY8wJx4%2FPz4%2B%2Bh5NAqc812cud5%2BKHBO4jSuHKAxXuXSOUm%2BHu4zNu8v2N6ngLYJWPpWd4VH%2FKKpYdfczUPTCLCYn4Dt3aw%3D%3D; _cc_id=5b72741f884ffc2320d4a337526c7b69; panoramaId_expiry=1723728230508; panoramaId=70a1b961cee42967de3e1a634bfc16d53938e30a9f9de054edbd7e730ad47bf3; panoramaIdType=panoIndiv; __gads=ID=4057fc116d25f8b2:T=1723123430:RT=1723123430:S=ALNI_Mb8kuvkOFn_a-QtEeJDbAQY7mXetg; __gpi=UID=00000eb942370eab:T=1723123430:RT=1723123430:S=ALNI_MZ6M0mzTHnuq07jC4pdALpQWCmegA; __eoi=ID=521a0147b5efb1e8:T=1723123430:RT=1723123430:S=AA-AfjanBNDOu7TdEftlLRNURQ1D; _clsk=m0laaq%7C1723123430736%7C1%7C0%7Cz.clarity.ms%2Fcollect; FCNEC=%5B%5B%22AKsRol9Bx5ID8cb5ZzHABF-KwQPGpwcf5ISbrKe-eGgT0xRH0r5x6Kd84GrBH1l5ZEXf9zA4dwV70PYdFUoVRrBEYuAsBNSBIrYnbzxtPaRBu9mZnZIzV2vR_Jg1zRgyZweMRqZcfQUvwLQuWx-fKAIeguMhINUTQw%3D%3D%22%5D%5D'
    }
data = requests.get(url,headers = header);
data.encoding = "utf-8";
data = data.text;


soup = BeautifulSoup(data,'html.parser');
allnews = soup.find(class_= "news_list");
news = allnews.find(class_="list");
items = news.find_all('li');

for row in items:
    
    if row.find('h2') != None:
    
        title = row.find('h2').text;
        
        link = row.find('a').get('href');
        time = row.find(class_='time').text;
        
        photo = row.find('img').get('data-original');
        
        if not('https' in link):
            link = 'https://news.tvbs.com.tw'+link;
        
        print(title);
        print(link);
        print(photo);
        print(time);
        print();
