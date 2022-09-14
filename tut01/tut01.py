#Function defined
def octact_identification(mod=5000):
    df.at[1,'Octant ID']="Mod "+str(mod)
#Created a list named range_list and added the range values in that
    range_list=[0]
    x=int(len(df)/mod)
    for i in range (x):
        range_list.append(mod*(i+1))
    range_list.append(len(df))
    for i in range(len(range_list)-1):
#Found out the counts of each i=octant in the range
        for octant in ['1','-1','2','-2','3','-3','4','-4']:
            df.at[2+i,octant]=df['Octant'].iloc[range_list[i]:range_list[i+1]].value_counts()[int(octant)]
#Range values are printed
        df.at[2+i,'Octant ID']=str(range_list[i])+" - "+ str(range_list[i+1]-1)
        
from platform import python_version
import pandas as pd
#Reading the input csv file
df = pd.read_csv("octant_input.csv")

#Finding mean of U,V,W and made a columns to add that
U_Avg  = df['U'].mean()
df['U Avg']=''
df.at[0,'U Avg']=U_Avg
V_Avg  = df['V'].mean()
df['V Avg']=''
df.at[0,'V Avg']=V_Avg
W_Avg  = df['W'].mean()
df['W Avg']=''
df.at[0,'W Avg']=W_Avg

#Calculated the U',V' and W' values and added into the column
df["U'=U - U avg"]=df['U']-df['U Avg'][0]
df["V'=V - V avg"]=df['V']-df['V Avg'][0]
df["W'=W - W avg"]=df['W']-df['W Avg'][0]

#Calculated the octant values and added into Octant column
df['Octant']=''
for i in range(len(df)):
    if df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]>0:
        df.at[i,"Octant"]=1
    elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]<0:
        df.at[i,"Octant"]=-1
    elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]>0:
        df.at[i,"Octant"]=2
    elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]<0:
        df.at[i,"Octant"]=-2
    elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]>0:
       df.at[i,"Octant"]=3
    elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]<0:
        df.at[i,"Octant"]=-3
    elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]>0:
       df.at[i,"Octant"]=4
    elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]<0:
        df.at[i,"Octant"]=-4

#defined columns to mach the template of given output csv files
df['']=''
df['Octant ID']=''
df['1']=''
df['-1']=''
df['2']=''
df['-2']=''
df['3']=''
df['-3']=''
df['4']=''
df['-4']=''
df.at[0,'Octant ID']="Octant Count"
df.reset_index(drop=True) 

#initialised values of count of each octant as 0 before finding total count of each octant
count1=0 #count of octant 1
counti=0 #count of octant -1
count2=0 #count of octant 2
countii=0 #count of octant -2
count3=0 #count of octant 3
countiii=0 #count of octant -3
count4=0 #count of octant 4
countiv=0 #count of octant -4

#Found out the count of each octant values
for i in range(len(df)):
    if df.at[i,'Octant'] == 1:
        count1+=1
    elif df.at[i,'Octant']==-1:
        counti+=1
    elif df.at[i,'Octant']==2:
        count2+=1
    elif df.at[i,'Octant']==-2:
        countii+=1
    elif df.at[i,'Octant']==3:
        count3+=1
    elif df.at[i,'Octant']==-3:
        countiii+=1
    elif df.at[i,'Octant']==4:
        count4+=1
    elif df.at[i,'Octant']==-4:
        countiv+=1

#Added the count of octant values into the cell
df.at[0,'1']=count1
df.at[0,'-1']=counti
df.at[0,'2']=count2
df.at[0,'-2']=countii
df.at[0,'3']=count3
df.at[0,'-3']=countiii
df.at[0,'4']=count4
df.at[0,'-4']=countiv
df.at[1,'']="User Input"

mod=5000 
#function call
octact_identification(mod)
#Made output csv file named Octant_output.csv

ver=python_version()
if ver=='3.8.10':
    print("Correct version installed")
else:
     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
df.to_csv('octant_output.csv', index=False)  

