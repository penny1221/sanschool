# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:56:16 2024

@author: USER
"""

def hello():
    print('你好');
    
def loopfor():
    for i in range(5):
        print(i);


def sumNumber():
    total = 0;
    for i in range(1,11):
        total += i;
    return total;
    
number = sumNumber();
print(number);
print(sumNumber());

#hello();#呼叫
