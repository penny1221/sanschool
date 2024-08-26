# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:04:14 2024

@author: USER
"""

import sqlite3;

conn = sqlite3.connect('wed.db');
cursor = conn.cursor();
# sql = "select * from student";
sql = "select name,sex from student";
cursor.execute(sql);
data = cursor.fetchall();
print(data);

for row in data:
    for item in row:
        print(item,end=",")
conn.close();