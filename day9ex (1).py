# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:40:23 2024

@author: USER
"""

def divfun(n1,n2):
    try:
        result = divmod(n1,n2);
        print(result);
    except Exception as e:
        print("fun處理");
        raise Exception(e);
try:
    divfun(10,0)
except Exception as e:
    print(e);