# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:06:32 2024

@author: USER
"""

def st(school,**personal):
    print(school,"依照學生姓名排序");
    print(sorted(personal));
    upsixty = {k:v for k,v in personal.items() if v >=60};
    print("及格人數",len(upsixty),"人");
    print(upsixty);
    print("及格人",sorted(upsixty));
st('中一中',Mary = 90,John = 30,bill = 60,sue = 42,com = 80,eric = 88,tom = 72);

