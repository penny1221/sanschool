# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:14:56 2024

@author: awun5
"""

t = list();
rows = int(input("請輸入幾列："));


for i in range(rows):#假設5
    r = [];#每個陣列儲存一行因此需要多個陣列
    for j in range(i + 1):#每行的數字為 i+1個
        if( j == 0 or j == i):#最開始輸出一，結尾輸出一，若i值=j值為最後輸出數字
            r.append(1);
        else:
            #print(t[i-1][j-1] ,t[i-1][j]);
            r.append(t[i-1][j-1] + t[i-1][j]);#位置相加
    t.append(r);#每行跑完後放入陣列中

for a in range(rows):
    for b in range(a+1):
        print(t[a][b],end=" ");
    print(" ");