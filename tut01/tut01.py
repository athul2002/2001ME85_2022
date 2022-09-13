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
df.to_csv('octant_output.csv', index=False)  
df.reset_index(drop=True)  

#def octact_identification(mod=5000):
    

#mod=5000
#octact_identification(mod)