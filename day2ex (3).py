# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:02:05 2024

@author: USER
"""

score = int(input("請輸入分數:"));

#可做防呆
if(score <= 200):
    print("丁");

elif(score <= 400):
    print("丙");

elif(score <= 500):
    print("乙");

else:
    print("甲");
    
print("完成");