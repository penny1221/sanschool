# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:34:21 2024

@author: USER
"""

data =[1,2,3];
num1,num2 = eval(input("2個值，隔開："));

try:
    result = num1 / num2;
    print(result);
    print(data[0]);
    print(data[10]);
except IndentationError :
    print("索引值錯誤");
    print("請檢查");
except:
    print("其他錯誤");
print("finsh");