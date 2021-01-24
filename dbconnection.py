# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:52:17 2020

@author: deesaw
"""


import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    sqliteConnection=create_connection()
    cursor = sqliteConnection.cursor()
    thedata = open('lookup.txt', 'rb').read()
    sql = "INSERT INTO sometable (theblobcolumn) VALUES (%s)"
    cursor.execute(sql, (thedata,))
#    query="""CREATE TABLE dbo.Imagess([ImageID] [int] IDENTITY(1,1) NOT NULL,   [ImageName] [varchar](40) NOT NULL,
#                [OriginalFormat] [nvarchar](5) NOT NULL,  [ImageFile] [varbinary](max) NOT NULL)  """

    cursor.execute(query)
    sqliteConnection.commit()