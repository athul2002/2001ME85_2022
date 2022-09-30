from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count():
    for i,x in enumerate(['1','-1','2','-2','3','-3','4','4']):
        df.at[i,'octant']=x
    for j,octval in enumerate([1,-1,2,-2,3,-3,4,-4]):
        count=0
        maxi=0
        for i in range(len(df['Octant'])):
            if df['Octant'][i]==octval:
                count+=1
                maxi=max(count,maxi)
            else:
                count=0
            

from platform import python_version
ver = python_version()
import pandas as pd
#Reading the input csv file
df = pd.read_excel("input_octant_longest_subsequence.xlsx")

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
df['']=''
df['octant']=''
df['Subsequent']=''
df['Count']=''
if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
octant_longest_subsequence_count()
df.to_excel('output_octant_transition_identify.xlsx', index=False)  

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

