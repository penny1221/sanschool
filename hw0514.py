# -*- coding: utf-8 -*-
"""
Created on Wed May 15 12:07:22 2024

@author: awun5
"""

'''
隨機產生1~49之間的數
1-1 黑名單:不可以被新增進去 10 15 39
1-2 請使用random的方式來自動新增這六個數字
1-3 白名單:一定要有17、41
'''
import random;

number = list();
b = [10,15,39];
w = [17,41];

while(True):
    num = random.randrange(1,50);
    number.append(num)
    #print("產生",number);
    for i in range(0,len(b)):
        if(number.count(b[i]) == 1):
            number.remove(b[i]);
            #print("刪除",number);
            continue;

    if( len(number) == 6):
        for j in range(0,len(w)):
            if(number.count(w[j]) == 0):
                number.pop(0);
                number.append(w[j]);
                #print("add白名單",number);
        break;
                
        
print(number);

'''
    if(number.count(10) == 1):
        number.remove(10);
        print("移除後",number);
    if(number.count(15) == 1):
        number.remove(15);
        print("移除後",number);
    if(number.count(39) == 1):
        number.remove(39);
        print("移除後",number);
'''