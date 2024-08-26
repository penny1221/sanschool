# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv;

fn = "member.csv";

with open(fn,encoding="utf-8") as fobj:
    csvreader = csv.reader(fobj);
    data = list(csvreader);

print(data);