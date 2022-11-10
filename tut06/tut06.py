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
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
    except:
        print("Unable to send mail. Check the credentials.")
def attendance_report():
    try:
        #creating a list of roll numbers
        roll_nums = [str(i) for i in df1['Roll No']]
        #creating a set containing dates of all mondays and thursdays
        set_date=({datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").date() for i in df['Timestamp']  if datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").strftime('%a') in ['Mon','Thu']})
        #converting the set of dates into a list 
        list_date=list(set_date)
        #sorting the list containing dates
        list_date.sort()
        #making a dictionary named attendance
        #inside the dictionary, for each roll number another dictionary is made which contains the date.
        #inisde the date dictionary, the value of real is added by 1 if present and similarly for invalid and duplicate
        attendance={rollno:{date:{'real':0,'invalid':0,'duplicate':0,} for date in list_date} for rollno in roll_nums}
        for i in range(len(df['Timestamp'])):
            d = (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M')).date()
            rollno=(str(df['Attendance'][i])).split(" ")[0]
            if (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').weekday() == 0 or datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').weekday() == 3):
                if datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').hour==14 or (datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').hour==15 and datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M').minute==00):
                    #when its a monday or thursday and between 2:00pm-3:00pm this loop runs
                    rollno=(str(df['Attendance'][i])).split(" ")[0]
                    if rollno == 'nan' or rollno not in roll_nums:
                        continue
                    #if the real attendance of a particular roll number is zero for that date, real value is increased by 1
                    if attendance[rollno][d]['real']==0:
                        attendance[rollno][d]['real']+=1
                    else:
                    #if real value is not zero, value of duplicate is added by 1
                        attendance[rollno][d]['duplicate']+=1
                else:
                    #when attendance is marked other than during lecture hour, invalid value is increased by 1
                    attendance[rollno][d]['invalid']+=1
            else:
                continue 
    except:
        print("An error occured while calculating attendance.")
    dfi=pd.DataFrame()
    dfi.at[0,'Date']=''
    try:
        for i in range(len(df1['Roll No'])):
            dfi.at[0,'Roll']=df1['Roll No'][i]
            dfi.at[0,'Name']=df1['Name'][i]  
            count=1
            real_count=0
            #total_real is for finding total real attendnace
            total_real=0
            #total_duplicate is for finding total duplicate attendnace
            total_duplicate=0
            #total_invalid is for finding total invalid attendnace
            total_invalid=0
            for date in list_date:
                dfi.at[count,'Date']=date
                #printing Total attendance one person marked on  a day as the sum of invalid, real and duplicate attendnace on that day
                dfi.at[count,'Total Attendance']=attendance[df1['Roll No'][i]][date]['real']+attendance[df1['Roll No'][i]][date]['duplicate']+attendance[df1['Roll No'][i]][date]['invalid']
                #printing the real attendnace count on day               
                dfi.at[count,'Real']=attendance[df1['Roll No'][i]][date]['real']
                total_real+=attendance[df1['Roll No'][i]][date]['real']
                #printing count of duplictae attendnace on a day
                dfi.at[count,'Duplicate']=attendance[df1['Roll No'][i]][date]['duplicate']
                total_duplicate+=attendance[df1['Roll No'][i]][date]['duplicate']
                #printing count of invalid attendance count
                dfi.at[count,'Invalid']=attendance[df1['Roll No'][i]][date]['invalid']
                total_invalid+=attendance[df1['Roll No'][i]][date]['invalid']
                #printing 1 in absent column if real column value is 0
                dfi.at[count,'Absent']=1-attendance[df1['Roll No'][i]][date]['real']
                count+=1
                dfc.at[i,'Roll']=df1['Roll No'][i]
                dfc.at[i,'Name']=df1['Name'][i]

                #marking present as P and absent and A            
                if attendance[df1['Roll No'][i]][date]['real']==1:
                    dfc.at[i,date]='P'
                    real_count+=1
                else:
                    dfc.at[i,date]='A'
            dfc.at[i,'Actual Lecture Taken']=len(list_date)
            dfc.at[i,'Total Real']=real_count
            dfc.at[i,'Percentage']=round((real_count/len(list_date))*100,2)
            dfi.at[0,'Real']=total_real
            dfi.at[0,'Duplicate']=total_duplicate
            dfi.at[0,'Invalid']=total_invalid
            dfi.at[0,'Absent']=len(list_date)-total_real
            dfi.to_excel('./output/' + df1['Roll No'][i] + '.xlsx',index=False)
    except:
        print("An error occured while printing.")
from platform import python_version
ver = python_version()
try:
    import pandas as pd
    try:
        df1=pd.read_csv("input_registered_students.csv")
        df=pd.read_csv("input_attendance.csv")
        if ver == "3.8.10":
            print("Correct Version Installed")
        else:
            print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
        dfc = pd.DataFrame()
        list_fake=[]
        list_actual=[]
        try:
            #function call for making attendance report
            attendance_report()
        except:
            print("Function not defined.")
        dfc.to_excel('./output/attendance_report_consolidated.xlsx',index=False)
        try:
            #function call for sending mail
            send_mail()
        except:
            print("Mail function not found.")
    except FileNotFoundError:
        print("File not found. Please try again.")
except ModuleNotFoundError:
    print("Module not found!")

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
