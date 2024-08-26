# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:30:15 2024

@author: USER
"""
import csv;

fn = "member.csv";

with open(fn,encoding="utf-8") as fobj:
    csvdic = csv.DictReader(fobj);
    
    for row in csvdic:
        print(row);
        print(row["name"]);
        print(row["tel"]);
        print();