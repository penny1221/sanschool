# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:30:34 2024

@author: USER
"""

st = {'jhon':40,'peter':70,'mary':51,'eric':43,'bill':88};
upsixty = {k:v for k,v in st.items() if v >= 60};
lowsixty = {k:v for k,v in st.items() if v < 60};
print(upsixty);
print(lowsixty);