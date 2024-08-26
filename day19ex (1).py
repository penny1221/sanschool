# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3;

conn = sqlite3.connect('wed.db');



sql = "create table student(sid integer primary key autoincrement,name varchar(30),sex varchar(2),address varchar(100))"

cursor = conn.cursor();
cursor.execute(sql);
conn.commit();#立即提交 若無這項指令資料只會暫存
conn.close();