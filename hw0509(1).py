# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:29:42 2024

@author: awun5
"""
"""
亂數產生5~100之間可以被五整除的數，產生五個且不可重複
nu請用五個變數去儲存
"""
import random;

num1 = 0;
num2 = 0;
num3 = 0;
num4 = 0;
num5 = 0;

for i in range(1,1000): 
    num = random.randrange(5,101,5);
    
    if( i == 1):
        num1 = num;
       
    else:
        if(num2 == 0):
            if(num != num1):
                num2 = num;             
        elif(num3 == 0):
            if(num != num1 and num != num2):
                num3 = num
        elif(num4 == 0):
            if(num != num1 and num != num2 and num != num3):
                num4 = num
        elif(num5 == 0):
            if(num != num1 and num != num2 and num != num3 and num != num4):
                num5 = num
        else:
         break;
print("第一個數=",num1," 第二個數=",num2," 第三個數=",num3," 第四個數=",num4," 第五個數=",num5,sep="");