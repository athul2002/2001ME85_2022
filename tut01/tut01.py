import pandas as pd
df = pd.read_csv("D:\\ONEDRIVE\\Documents\\GitHub\\2001ME85_2022\\tut01\\octant_input.csv")
U_Avg  = df['U'].mean()
df['U Avg']=''
df['U Avg'][0]=U_Avg
V_Avg  = df['V'].mean()
df['V Avg']=''
df['V Avg'][0]=V_Avg
W_Avg  = df['W'].mean()
df['W Avg']=''
df['W Avg'][0]=W_Avg
df["U'=U - U avg"]=df['U']-df['U Avg'][0]
df["V'=V - V avg"]=df['V']-df['V Avg'][0]
df["W'=W - W avg"]=df['W']-df['W Avg'][0]
df['Octant']=''
for i in range(len(df)):
    if df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]>0:
        df["Octant"][i]=1
    elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]<0:
        df["Octant"][i]=-1
    elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]>0:
        df["Octant"][i]=2
    elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]<0:
        df["Octant"][i]=-2
    elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]>0:
        df["Octant"][i]=3
    elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]<0:
        df["Octant"][i]=-3
    elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]>0:
        df["Octant"][i]=4
    elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]<0:
        df["Octant"][i]=-4
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
df['Octant ID'][0]="Octant Count"
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
    if df['Octant'][i]==1:
        count1+=1
    elif df['Octant'][i]==-1:
        count11+=1
    elif df['Octant'][i]==2:
        count2+=1
    elif df['Octant'][i]==-2:
        count22+=1
    elif df['Octant'][i]==3:
        count3+=1
    elif df['Octant'][i]==-3:
        count33+=1
    elif df['Octant'][i]==4:
        count4+=1
    elif df['Octant'][i]==-4:
        count44+=1
df['1'][0]=count1
df['-1'][0]=count11
df['2'][0]=count2
df['-2'][0]=count22
df['3'][0]=count3
df['-3'][0]=count33
df['4'][0]=count4
df['-4'][0]=count44
df.to_csv('octant_output.csv', index=False)  
#def octact_identification(mod=5000):
    

#mod=5000
#octact_identification(mod)