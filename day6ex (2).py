# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:18:04 2024

@author: USER
"""

st = {'周子瑜':92,'IU':89};
name = input("輸入姓名:");

if name in st:
    print(name,"的成績",st[name]);
else:
    score = int(input("輸入分數:"));
    st[name] = score;
print(st);
keys = st.keys();
values = st.values();
print(keys);
print(values);
