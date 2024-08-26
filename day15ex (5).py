# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:40:19 2024

@author: USER
"""

import csv;

fn = "test.csv";

data = [['A'],['B'],['C']]

with open(fn,'w',encoding="utf-8",newline='') as fobj:
    csvwriter = csv.writer(fobj,delimiter="\t");
    csvwriter.writerows(data);