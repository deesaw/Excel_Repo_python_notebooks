# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:48:26 2020

@author: deesaw
"""

import glob
import pandas as pd
files=glob.glob('*.txt')
pf={}
for i,f in enumerate(files):
    pf[i]=pd.read_csv(f,sep='\t',dtype='object')
print(pf[0])
def lookup(d,legacy,transformed):
    b=None
    word = input("Word to lookup: ")
    for fruit in d[legacy]:
        if str(fruit) == str(word):
            b= d[d[legacy]==fruit][transformed]
    return b

a = lookup(pf[0],'legacy','xref')
print(a.values)

