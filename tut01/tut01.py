import pandas as pd
df = pd.read_csv("D:\\ONEDRIVE\\Documents\\GitHub\\2001ME85_2022\\tut01\\octant_input.csv")
#def octact_identification(mod):

U_Avg  = df['U'].mean()
df['U Avg']=''
df.at[0,'U Avg']=U_Avg
V_Avg  = df['V'].mean()
df['V Avg']=''
df.at[0,'V Avg']=V_Avg
W_Avg  = df['W'].mean()
df['W Avg']=''
df.at[0,'W Avg']=W_Avg
df["U'=U - U avg"]=df['U']-df['U Avg'][0]
df["V'=V - V avg"]=df['V']-df['V Avg'][0]
df["W'=W - W avg"]=df['W']-df['W Avg'][0]
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
count1=0
count2=0
count3=0
count4=0
count11=0
count22=0
count33=0
count44=0 
for i in range(len(df)):
    if df.at[i,'Octant'] == 1:
        count1+=1
    elif df.at[i,'Octant']==-1:
        count11+=1
    elif df.at[i,'Octant']==2:
        count2+=1
    elif df.at[i,'Octant']==-2:
        count22+=1
    elif df.at[i,'Octant']==3:
        count3+=1
    elif df.at[i,'Octant']==-3:
        count33+=1
    elif df.at[i,'Octant']==4:
        count4+=1
    elif df.at[i,'Octant']==-4:
        count44+=1
df.at[0,'1']=count1
df.at[0,'-1']=count11
df.at[0,'2']=count2
df.at[0,'-2']=count22
df.at[0,'3']=count3
df.at[0,'-3']=count33
df.at[0,'4']=count4
df.at[0,'-4']=count44
df.at[1,'']="User Input"
#mod=input()  

#octact_identification(mod)
df.to_csv('octant_output.csv', index=False)  

