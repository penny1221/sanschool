# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 100;
b = a ;

print(id(a));
print(id(b));

a = 199;
print(id(a));

item = [10,20,30,40]
data = item;
print(id(item));
print(id(data));
item[0] = 199;
print(data);
print(id(data));