# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:43:51 2024

@author: USER
"""

import os;

path = os.path.join("c:\\","good");

if os.path.exists(path):
    print("路徑存在");

else:
    os.mkdir(path);
    print("資料夾建立成功");