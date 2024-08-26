# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:20:52 2024

@author: USER
"""
def st(n,*s,sub=5):
    if(sub >= 1):
        print("姓名:",n);
        print('共有',sub,'科分數:',s);
    total = sum(s);
    print('總分:',total,'平均:%.3f'%(total/sub));
st('Mary',63,73,82,100,70);
st('jhon',81,92,33,sub = 3);