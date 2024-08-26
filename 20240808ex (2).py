# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup;
import requests

url = "https://www.setn.com/ViewAll.aspx";

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Cookie':'__htid=b4ed551d-b362-4a12-b7a7-4ec7800022dd; _ht_em=1; userKey=f15bd6c7-0033-420c-838b-f20a0b1bf1a9; AviviD_uuid=8a563826-b74f-43f8-9e4b-1314a3ed0779; AviviD_refresh_uuid_status=1; webuserid=2891bd48-7233-ddaf-979f-03fae3839325; AviviD_already_exist=0; AviviD_sw_version=1.0.868.210701; show_avivid_native_subscribe=1; _ga=GA1.1.1903727004.1723118429; _ga_8NJ3QZRCY6=GS1.1.1723118429.1.0.1723118429.60.0.0; ch_tracking_uuid=1; _fbp=fb.1.1723118429445.885829661170302729; AviviD_tid_rmed=1; _ht_47b240=1; _cc_id=5b72741f884ffc2320d4a337526c7b69; panoramaId_expiry=1723723230065; panoramaId=70a1b961cee42967de3e1a634bfc16d53938e30a9f9de054edbd7e730ad47bf3; panoramaIdType=panoIndiv; stid=1903727004.1723118429; _ga_54ZJR9ZRH0=GS1.1.1723118429.1.0.1723118431.58.0.0; __gads=ID=2ed043e4a0d2b9ae:T=1723118429:RT=1723118429:S=ALNI_MbNVx4qAZRxFYuDiohe3GpiHxbtdQ; __gpi=UID=00000eb935b80d03:T=1723118429:RT=1723118429:S=ALNI_MarIaDMMwgCcWc4qRKEHYIiZg4-JA; __eoi=ID=8d50a94b9c2b1e60:T=1723118429:RT=1723118429:S=AA-AfjYguCg3ZxSdvlWm8BEuuyaz; stid2=1903727004.1723118429; FCNEC=%5B%5B%22AKsRol_fCuZkDXQLWhFUi52ETDIVe2q2RKgpWcQvGaw2-zFf_Dbip0KSTr2-CwZWIWkk274n6YGHxEcrKdzrgKPYFj_y9S8lODSVUOp320v2-z9Vsnsn8tsZboIZWmpeJjhIEKGzDLx1Hx65dAP0EH_ULSJacW934A%3D%3D%22%5D%5D'
    }
data = requests.get(url,headers = header);
data.encoding = "utf-8";
data = data.text;
#通常到此要進行確認是否有東西可以爬
#print(data);

soup = BeautifulSoup(data,'html.parser');


allnews = soup.find(id="NewsList");
times = allnews.find_all('time');
h3s = allnews.find_all('h3');

if len(times) == len(h3s): #確保兩者長度相同   
    for i in range(len(times)):
        time = times[i].text;
        title = h3s[i].text;
        link = h3s[i].find('a').get('href');
        
        if not('https' in link):
            link = 'https://www.setn.com/'+link;
            
        print(time);
        print(title);
        print(link);
        print();
        
else:
    print('error');
        