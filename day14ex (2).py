# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:40:15 2024

@author: USER
"""

import datetime;
import os;

def writelog(error):
    today = datetime.datetime.today();
    file = datetime.datetime.strftime(today,'%y%m%d')+".log";
  
    path = os.path.join("c:\\", "lcc",file);
    
    with open(path,'a',encoding="utf-8") as fobj:
        time = datetime.datetime.strftime(today,'%H:%M:%S');
        fobj.write(time+"\t");
        fobj.write(error+"\n");

try:
    score = [90,70,10,100];
    
    print(score[0]);
    print(score[10]);
    
except Exception as err:
    writelog(str(err));

print("程式執行完畢");
