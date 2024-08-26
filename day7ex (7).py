# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:25:48 2024

@author: USER
"""

def circle(r=10):
    area = r * r * 3.14 ;
    cl = 2 * r * 3.14;
    return area , cl;
a,c = circle();
ac = circle(5);
print(a);
print(c);