# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:27:50 2024

@author: USER
"""

st = {'john':81,'peter':62};
st['bill'] = 100;
print(st);
st.update({'mary':83,'sue':92})
print(st);

print("排序");
for k in sorted(st):
    print('%-12s %3d'%(k,st[k]));
st.pop('john');
for k in sorted(st,reverse=True):
    print('%-12s %3d'%(k,st[k]));
print("清空字典",st.clear());
st.update(Eric=92,George = 73);
print(st);