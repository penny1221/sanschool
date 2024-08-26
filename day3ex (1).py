# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:31:48 2024

@author: USER
"""

"break跳脫迴圈 continuer跳下一個敘述"
for i in range(100):
    if i==15:
        break;
    if i%3 == 0:
        continue;
    print("i=",i);
    print("平方:",i*i);
print("finish");