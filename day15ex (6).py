# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:14:14 2024

@author: USER
"""

import csv

fn = "st.csv";

with open(fn,'w',encoding="utf-8",newline='') as fobj:
    fields = ['name','sex','tel'];
    dictw = csv.DictWriter(fobj, fieldnames = fields);
    dictw.writerow({'name':'王大德','sex':'男','tel':'0912666999'});
    dictw.writerow({'name':'王依依','sex':'女','tel':'0912656229'});

