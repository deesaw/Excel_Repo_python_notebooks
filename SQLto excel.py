# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:11:13 2020

@author: deesaw
"""

import win32com.client 
import datetime as dt
import pandas as pd
import glob
import re

s = 'radkar'
def solution(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True

    return s == s[::-1]
  
solution(s)

def solution(x):
    string = str(x)
    
    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])
    
print(solution(-231))
print(solution(345))

def solution(s):
    # build hash map : character and how often it appears
    count = collections.Counter(s) # <-- gives back a dictionary with words occurrence count 
                                         #Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1

def searchword(e,d):
    e = re.sub('[^a-zA-Z0-9]',' ',e)  
    d = re.sub('[^a-zA-Z0-9]',' ',str(d))  
    s = e.split(" ") 
    if re.search(str(d), e.lower()):
        return True
    else:
        for i in s: 
            if (i.strip() == str(d).strip()) or (str(d).strip() in i.strip()):
                return True
        return False
def searchword1(e,d):
     e = re.sub('[^a-zA-Z0-9]',' ',e)  
     d = re.sub('[^a-zA-Z0-9]',' ',str(d)) 
     d1=d+'$'
     s = e.split(" ")
     if re.search(d1, e.lower()):
         return True
     else:
        for i in s: 
            if (i.strip() == str(d).strip()) or (str(d).strip() in i.strip()):
                return True
        return False

myFiles = glob.glob('*.xlsx')
for file in myFiles:
    print(file)
    df=pd.read_excel(file,header=0,dtype=object)
day=int(input("Number of days to be considered:"))
y = (dt.date.today() - dt.timedelta(days=day))
print(y)
y = y.strftime('%m/%d/%Y %H:%M %p')
print(y)

outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
namespace = outlook.Session
recipient = namespace.CreateRecipient("deesaw@deloitte.com")
inbox = outlook.GetDefaultFolder(6)#(recipient, 6)
messages = inbox.Items
messages = messages.Restrict("[ReceivedTime] >= '" + y +"'")
email_subject = []

for x in messages:
    sub = x.Subject
    PCOOO='Task UID'
    if PCOOO in sub:
        if '92785' in sub:
            print(sub)
            print(searchword1(sub,'92785'))
            print(searchword1(sub,'#done'))
            print(searchword1(sub,'#start'))
            print(searchword1(sub,'#issue'))
        email_subject.append(sub)
        








