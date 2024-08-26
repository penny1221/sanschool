# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:17:44 2024

@author: USER
"""

import csv;

fn = "member.csv";

with open(fn,encoding="utf-8") as fobj:
    csvreader = csv.reader(fobj);
    for row in csvreader:
        print("Row %s ="%csvreader.line_num,row);
        print(row[2]);
        for item in row:
            print(item);
        print();