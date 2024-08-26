# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:11:59 2024

@author: USER
"""

import sqlite3;

conn = sqlite3.connect('wed.db');
cursor = conn.cursor();
sql = "update student set address='台南市國華一街' where sid = 1"
cursor.execute(sql);
conn.commit();
conn.close();