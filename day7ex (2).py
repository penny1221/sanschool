# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:12:00 2024

@author: USER
"""

data = list();
for i in range(1,11):
    data.append(i);
print(data);
#精簡
level = [i for i in range(1,11)];
print(level);
level = [i for i in range(1,11) if i % 3 == 0];
print(level);