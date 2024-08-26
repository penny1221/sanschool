# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:48:18 2024

@author: USER
"""

def divfun(num1,num2):
    try:
      result = divmod(num1,num2);
    except:
         #print("捕獲error");
         pass;
    else:
        print(result);
        
    finally:
        print("finish");
divfun(100, 32);
divfun(10, 2);
divfun(20, 0);