# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:29:19 2020

@author: deesaw



thedata = open('thefile', 'rb').read()
sql = "INSERT INTO sometable (theblobcolumn) VALUES (%s)"
cursor.execute(sql, (thedata,))
"""
import sqlite3
conn = sqlite3.connect("mydatabase.db")#connecting to a database
cursor = conn.cursor()
# create a table
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
"""
#cursor.execute('CREATE TABLE blobcheck
#                  (Id int, filename text, file BLOB)')

print("Table Created")
"""
c=convertToBinaryData("C:\\Users\\deesaw\\Desktop\\Image_Search\\Images\\images\\1163.jpg")
#cursor = conn.cursor()
b=(1,'1163.jpg',str(c))
script=("INSERT INTO blobcheck VALUES (?,?,?)",b)
print("inserted")
cursor.execute(script)
conn.close()

