# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:21:04 2024

@author: USER
"""
#將重複的刪除 使用迴圈
data = [1,2,3,'a','b','b',1]

t = list();

for i in data:
    if not(i in t):
        t.append(i);
        
print(t);

#費式數列
