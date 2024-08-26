# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:12:02 2024

@author: USER
"""
import sqlite3;

conn = sqlite3.connect('wed.db');
cursor = conn.cursor();
sql = "delete from students where sid=1"
cursor.execute(sql);
conn.commit();
conn.close();
