from datetime import datetime
start_time = datetime.now()

def attendance_report():
    roll_nums = [str(i) for i in df1['Roll No']]
    set_date=({datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").date() for i in df['Timestamp']  if datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").strftime('%a') in ['Mon','Thu']})
    list_date=list(set_date)
    list_date.sort()
    attendance={rollno:{date:{'actual':0,'invalid':0,'duplicate':0,} for date in list_date} for rollno in roll_nums}
    for i in range(len(df['Timestamp'])):
        d = (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M')).date()
        rollno=(str(df['Attendance'][i])).split(" ")[0]
        if (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').weekday() == 0 or datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').weekday() == 3):
            if datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').hour==14 or (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').hour==15 and datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').minute==00):
                rollno=(str(df['Attendance'][i])).split(" ")[0]
                if rollno == 'nan' or rollno not in roll_nums:
                    continue
                if attendance[rollno][d]['actual']==0:
                    attendance[rollno][d]['actual']+=1
                else:
                    attendance[rollno][d]['duplicate']+=1
                    print(rollno)
            else:
                attendance[rollno][d]['invalid']+=1
        else:
            continue 
    dfi=pd.DataFrame()
    dfi.at[0,'Date']=''
    
    for i in range(len(df1['Roll No'])):
        dfi.at[0,'Roll']=df1['Roll No'][i]
        dfi.at[0,'Name']=df1['Name'][i]  
        count=1
        real_count=0
        for date in list_date:
            dfi.at[count,'Date']=date
            dfi.at[count,'Total Attendance']=attendance[df1['Roll No'][i]][date]['actual']+attendance[df1['Roll No'][i]][date]['duplicate']+attendance[df1['Roll No'][i]][date]['invalid']
            dfi.at[count,'Real']=attendance[df1['Roll No'][i]][date]['actual']
            dfi.at[count,'Duplicate']=attendance[df1['Roll No'][i]][date]['duplicate']
            dfi.at[count,'Invalid']=attendance[df1['Roll No'][i]][date]['invalid']
            dfi.at[count,'Absent']=1-attendance[df1['Roll No'][i]][date]['actual']
            count+=1
            dfc.at[i,'Roll']=df1['Roll No'][i]
            dfc.at[i,'Name']=df1['Name'][i]
            if attendance[df1['Roll No'][i]][date]['actual']==1:
                dfc.at[i,date]='P'
                real_count+=1
            else:
                dfc.at[i,date]='A'
        dfc.at[i,'Real']=len(list_date)
        dfc.at[i,'Total Real']=real_count
        dfc.at[i,'Percentage']=round((real_count/len(list_date))*100,2)
        dfi.to_excel('./output/' + df1['Roll No'][i] + '.xlsx',index=False)

from platform import python_version
ver = python_version()
import pandas as pd
df1=pd.read_csv("input_registered_students.csv")
df=pd.read_csv("input_attendance.csv")
if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
dfc = pd.DataFrame()
list_fake=[]
list_actual=[]
roll_nums = [str(i) for i in df1['Roll No']]
attendance_report()
dfc.to_excel('./output/attendance_report_consolidated.xlsx',index=False)
#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
