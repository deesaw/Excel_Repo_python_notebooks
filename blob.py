
"""
from hdbcli import dbapi
Use the connect method:
dbapi.connect(host='localhost', port=30015, user='system', password='manager')
Example
"""
import pyodbc
import pandas as pd
conn = pyodbc.connect("Driver={SQL Server};"
                              "Server=ussltcsnw1940.solutions.glbsnet.com;"
                              "Database=DATAFIRST;"
                              "UID=deesaw;"
                              "PWD=Welcome@123")

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
c=convertToBinaryData("C:\\Users\\deesaw\\Desktop\\Image_Search\\Images\\images\\1163.jpg")
cursor = conn.cursor()
script="INSERT INTO dbo.Imagess(ImageName,OriginalFormat,ImageFile) values( 'Sample Image','jpg',"+str(c)+");"

cursor.execute(script)
"""
list=[
'tvMARA_Relevancy_All_ManufacturerParts_MFRNR_Missing_Rpt',
,'tvMARC_Buy_Material_EKKO_BSTYP_K_Contract_Missing_Rpt'
,'tv_MARC_BESKZ_AUSSS_INHOUSE_NO_ASSEMBLYSCRAP_Rpt'
,'tvMARA_Stock_Material_PSTAT_L_HasStorageView_LGNUM_Blank_NoWarehouse_Rpt'
     ]

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
    writer = pd.ExcelWriter(excelname)
    df.to_excel(writer, sheet_name='bar',index=False)
    writer.save()
"""