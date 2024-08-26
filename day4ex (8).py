# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:57:33 2024

@author: USER
"""

words = ['a','b','a','c','d','a','c','f']
a = words.count('a');
f = words.count('f');
g = words.count('g');
b = words.count('b');
c = words.count('c');

print(a);
print(f);
print(g);
print(b);
print(c);

ind = words.index('d');

print("'d'index=",ind);

start = 0;
for i in range(words.count("c")):
    ind = words.index("c",start);
    print("c的索引:",ind);
    start = ind+1;