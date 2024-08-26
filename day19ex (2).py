# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:40:30 2024

@author: USER
"""

import sqlite3;

conn = sqlite3.connect('wed.db');
cursor = conn.cursor();

sql = '''
insert into student(name,sex,address) values('bill','m','台中一中')
'''
cursor.execute(sql);
conn.commit();
conn.close();