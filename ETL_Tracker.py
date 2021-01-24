import win32com.client 
import datetime as dt
import pandas as pd
import glob
import re

def searchword(e,d):
    e = re.sub('[^a-zA-Z0-9]','',e)  
    d = re.sub('[^a-zA-Z0-9]','',str(d))  
    s = e.split(" ") 
    if re.search(str(d), e.lower()):
        return True
    else:
        for i in s: 
            if (i.strip() == str(d).strip()) or (str(d).strip() in i.strip()):
                return True
        return False
def searchword1(e,d):
     e = re.sub('[^a-zA-Z0-9]','',e)  
     d = re.sub('[^a-zA-Z0-9]','',str(d)) 
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
    xls = pd.ExcelFile(file)
    a=xls.sheet_names
    sheet_to_df_map = {}
    l=[]
    for sheet_name in a:
        sheet_to_df_map[sheet_name] = xls.parse(sheet_name,dtype=object)
        l.append(sheet_name)
        
    first_sheet=l[0]
    print(first_sheet)
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
        email_subject.append(sub)
        
df['#start']=None
df['#issue']=None
df['#done']=None
df['There']=None

df['UID']=df.apply(lambda x : re.sub('[^0-9a-zA-Z]','',str(x['UID'])),axis=1)
for d in df['UID']:
    print(d)
    if df.loc[df['UID']==d,'#done'].values[0] is True:
        print('*****************')
        print('*****************')
        continue;
    else:
        for e in email_subject:
            s=searchword(e,d) 
            df.loc[df['UID']==d,'There']=s  
            if s is True and '#' in e:#and (df.loc[df['UID']==d,'#done'] is False or df.loc[df['UID']==d,'#done'] is None):
                done=searchword1(e.lower(),'#done')
                #print('done',done)
                issue=searchword1(e.lower(),'#issue')
                start=searchword1(e.lower(),'#start')
                df.loc[df['UID']==d,'#start']=start
                df.loc[df['UID']==d,'#issue']=issue
                df.loc[df['UID']==d,'#done']=done
                if df.loc[df['UID']==d,'#done'].values[0] is True:
                    break;


df['Tag Status']=df.apply(lambda x :  '#done' if (x['#done'] is True) else('#issue' if x['#issue'] else('#start' if x['#start'] else ('Received' if x['There'] else 'Yet to receive'))) ,axis=1)
#df=df.iloc[:,1:]
#df=df.iloc[:,1:]

#df.to_excel(file, sheet_name='ETL_Tracker', engine='xlsxwriter',index=False)
import os
path=os.path.join(os.getcwd(),file)
writer = pd.ExcelWriter( path,engine='xlsxwriter')
sheet_to_df_map[first_sheet]=df
for s,j in sheet_to_df_map.items():
    j.to_excel(writer,sheet_name=s,index=False)

writer.save()





