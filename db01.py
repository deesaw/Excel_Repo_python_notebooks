import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
sql = "SELECT * FROM blobcheck"
print ("listing of all the records in the table:")
l=[]
for row in cursor.execute(sql):
    l.append(row)
print(l)
 
print ("Results...")

cursor.execute(sql)
conn.close()