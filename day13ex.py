# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

file="yahoo.txt";

file_obj = open(file,encoding = "UTF8");

data = file_obj.read();

file_obj.close();

print(data);