# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:55:52 2024

@author: USER
"""

import openpyxl;
from openpyxl.chart import BarChart,Reference;

wb = openpyxl.Workbook();

ws = wb.active;

row = [['','2022年','2023年'],
       ["台北市",100,90],
       ["台中市",300,600],
       ["高雄市",450,300],
       ["宜蘭縣",200,150]];

for r in row:
    ws.append(r);
    
chart = BarChart();
chart.title = "綠色城市種樹統計";
chart.y_axis.title = '數量';
chart.x_axis.title = '地區';

data = Reference(ws,min_col=2,max_col=3,min_row=1,max_row=5);
chart.add_data(data,titles_from_data = True)
xtitle = Reference(ws,min_col = 1,min_row=2,max_row=5);
chart.set_categories(xtitle)
ws.add_chart(chart,'G1');
wb.save('demo5.xlsx');