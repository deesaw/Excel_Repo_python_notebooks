# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:18:40 2020

@author: deesaw
"""
import pyodbc
import pandas as pd
conn = pyodbc.connect("Driver={SQL Server};"
                              "Server=ussltcsnw1940.solutions.glbsnet.com;"
                              "Database=DATAFIRST;"
                              "UID=deesaw;"
                              "PWD=Welcome@123")
list=[
'tv_BANKL_is_not_used'     ]

for v in list:
    print(v)
    script="select * from dbo."+v+";"
    cursor = conn.cursor()
    script="select * from dbo."+v 
    cursor.execute(script)
    rows=cursor.fetchall() 
    names = [desc[0] for desc in cursor.description] 
    df = pd.DataFrame([tuple(t) for t in rows]) 
    df.columns=names
    print(df.shape)
    excelname=v+'.xlsx'
    df.to_excel(excelname, sheet_name='v',index=False)