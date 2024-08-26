# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:07:30 2024

@author: USER
"""

import requests
import io
import xml.sax

class bushandler(xml.sax.ContentHandler):
    def startElement(self, tag, attrs):
        if(tag == "Route"):#抓xml標籤
            print(attrs['nameZh']);
            print(attrs['ddesc']);
            print(attrs['departureZh']);
            print();


if __name__ == '__main__':
    url="https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml"
    parser = xml.sax.make_parser(); #建立一個空的解析器
    bus = bushandler(); #規則
    parser.setContentHandler(bus);#透過空的解析器把規則顯現出來
    data = requests.get(url);
    data.encoding = "utf-8";
    data = data.text;
    f = io.StringIO(data);
    parser.parse(f);#解析
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        