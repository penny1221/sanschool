# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime;

today = datetime.datetime.today();
today2 = datetime.date.today();
print(today);
print(today2);

f = datetime.datetime.strftime(today,'%Y%m%d%H%M%S');
f2 = datetime.datetime.strftime(today,'%y%m%d');
print(f);
print(f2);