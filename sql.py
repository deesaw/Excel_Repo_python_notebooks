# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:18:44 2020

@author: deesaw
"""
import collections



text="My My Deepu Deepa Deepp"
text1=text.split()
print(text1)
t=collections.Counter(text1)
print(t)