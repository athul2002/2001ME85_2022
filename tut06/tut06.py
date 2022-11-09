from datetime import datetime
start_time = datetime.now()
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

def send_mail():
    subject = "Attendance report"
    body = "Attendnace report of students registered for CS384 course"
    sender_email = "xyz@gmail.com"
    receiver_email = "cs3842022@gmail.com"
    password = "changeMe"
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # Adding body to email
    message.attach(MIMEText(body, "plain"))
    # Opening file in binary mode
    with open('./output/attendance_report_consolidated.xlsx', "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    # Adding header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {'attendance_report_consolidated.xlsx'}",
    )
    # Adding attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def attendance_report():
    roll_nums = [str(i) for i in df1['Roll No']]
    set_date=({datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").date() for i in df['Timestamp']  if datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").strftime('%a') in ['Mon','Thu']})
    list_date=list(set_date)
    list_date.sort()
    attendance={rollno:{date:{'real':0,'invalid':0,'duplicate':0,} for date in list_date} for rollno in roll_nums}
    for i in range(len(df['Timestamp'])):
        d = (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M')).date()
        rollno=(str(df['Attendance'][i])).split(" ")[0]
        if (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').weekday() == 0 or datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').weekday() == 3):
            if datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').hour==14 or (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').hour==15 and datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').minute==00):
                rollno=(str(df['Attendance'][i])).split(" ")[0]
                if rollno == 'nan' or rollno not in roll_nums:
                    continue
                if attendance[rollno][d]['real']==0:
                    attendance[rollno][d]['real']+=1
                else:
                    attendance[rollno][d]['duplicate']+=1
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
            dfi.at[count,'Total Attendance']=attendance[df1['Roll No'][i]][date]['real']+attendance[df1['Roll No'][i]][date]['duplicate']+attendance[df1['Roll No'][i]][date]['invalid']
            dfi.at[count,'Real']=attendance[df1['Roll No'][i]][date]['real']
            dfi.at[count,'Duplicate']=attendance[df1['Roll No'][i]][date]['duplicate']
            dfi.at[count,'Invalid']=attendance[df1['Roll No'][i]][date]['invalid']
            dfi.at[count,'Absent']=1-attendance[df1['Roll No'][i]][date]['real']
            count+=1
            dfc.at[i,'Roll']=df1['Roll No'][i]
            dfc.at[i,'Name']=df1['Name'][i]
            if attendance[df1['Roll No'][i]][date]['real']==1:
                dfc.at[i,date]='P'
                real_count+=1
            else:
                dfc.at[i,date]='A'
        dfc.at[i,'Actual Lecture Taken']=len(list_date)
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
# send_mail()
#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
