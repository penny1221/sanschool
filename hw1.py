# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
1~100基數總和
1-1 可被7整除地數字總和
1-2 可被5和15同時整除的數
"""

total = 0;
total2 = 0;

print("可被5和15整除的數");

for i in range(1,101):
    if((i%2)==1):
        total+=i;
    if(i%7==0):
        total2+=i;
    if(i%5==0 and i%15==0):
        print(i);



print("1~100基數總和=",total);
print("1~100可被7整除數字總和=",total2);