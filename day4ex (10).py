# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:07:21 2024

@author: USER
"""

print('學生成績系統');
stu = [];
score = list();

while(True):
    q = input('請輸入姓名查成績(q離開):');
    if(q == 'q'):
        break;
    if(stu.count(q) ==1):
        ind = stu.index(q);
        print("stu:",stu[ind],"分數為:",score[ind]);
    else:
        ans = input("是否加入此學生(y/n)");
        if(ans.lower()=='y'):
            s = int(input("輸入分數"));
            stu.append(q);
            score.append(s);