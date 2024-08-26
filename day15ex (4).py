# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:40:19 2024

@author: USER
"""

import csv;

fn = "bike.csv";

with open(fn,'w',encoding="utf-8",newline='') as fobj:
    csvwriter = csv.writer(fobj,delimiter="\t");
    csvwriter.writerow(['sna','sbi','bemp']);
    csvwriter.writerow(['三重路口','10','31']);
    csvwriter.writerow(['總統府','30','2'])