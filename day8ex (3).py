# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def factorial(d,s):
    result = s;
    for i in d:
        result *= i;
    return result;
res = factorial(d = [3,5,7,11,13], s = 1);
print('結果:{:,}'.format(res));