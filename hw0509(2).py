# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:32:16 2024

@author: awun5
"""
"""
a,b,c三邊長
由使用者輸入邊常
判斷是不是為直角三角形
"""
a = int(input("請輸入邊長1:"));
b = int(input("請輸入邊長2:"));
c = int(input("請輸入邊長3:"));

if((a+b)>=c and (a+c)>=b and (c+b)>=a):
    print("可構成三角形");
    if((a*a)+(b*b)==(c*c) or (a*a)+(c*c)==(b*b) or (b*b)+(c*c)==(a*a)):
        print("可構成直角三角形");
    else:
        print("無法構成直角三角形");
else:
    print("不是三角形");
          

