from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/N6PBd4XdnEw
def octant_range_names(mod=5000):
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
    df.at[1,'Octant ID']="Mod "+str(mod)
    range_list=[0]
    x=int(len(df)/mod)
    for i in range (x):
        range_list.append(mod*(i+1))
    range_list.append(len(df))
    for i in range(len(range_list)-1):
        for octant in ['1','-1','2','-2','3','-3','4','-4']:
            df.at[2+i,octant]=df['Octant'].iloc[range_list[i]:range_list[i+1]].value_counts()[int(octant)]
        df.at[2+i,'Octant ID']=str(range_list[i])+" - "+ str(range_list[i+1]-1)  
    
    rank_list_overall_1=[]
    rank_list_overall_2=[]    
    for y in ['1','-1','2','-2','3','-3','4','-4']:
        rank_list_overall_1.append(df[y][0])
        rank_list_overall_2.append(df[y][0])
    rank_list_overall_2.sort(reverse=True)
    final_list_1=[]
    for i in range(0,len(rank_list_overall_2)):
        final_list_1.append((rank_list_overall_2.index(rank_list_overall_1[i]))+1)      

    for i in range(len(range_list)-1):
        mod_list_1=[]
        mod_list_2=[]
        for y in ['1','-1','2','-2','3','-3','4','-4']:
            mod_list_1.append(df[y][2+i])
            mod_list_2.append(df[y][2+i])
        mod_list_2.sort(reverse=True)
        final_list_2=[]
        for z in range(0,len(mod_list_2)):
            final_list_2.append((mod_list_2.index(mod_list_1[z]))+1)        
        for z in range(1,9):
            df.at[0,'Rank'+str(z)]=final_list_1[z-1] 
            df.at[2+i,'Rank'+str(z)]=final_list_2[z-1]    


from platform import python_version
ver = python_version()
import pandas as pd
df = pd.read_excel("octant_input.xlsx")

U_Avg  = df['U'].mean()
df.at[0,'U Avg']=U_Avg
V_Avg  = df['V'].mean()
df.at[0,'V Avg']=V_Avg
W_Avg  = df['W'].mean()
df.at[0,'W Avg']=W_Avg

df["U'=U - U avg"]=df['U']-df['U Avg'][0]
df["V'=V - V avg"]=df['V']-df['V Avg'][0]
df["W'=W - W avg"]=df['W']-df['W Avg'][0]

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
df.at[0,'Octant ID']="Overall Count"
df.reset_index(drop=True) 
count1,counti,count2,countii,count3,countiii,count4,countiv=0,0,0,0,0,0,0,0

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

df.at[0,'1']=count1
df.at[0,'-1']=counti
df.at[0,'2']=count2
df.at[0,'-2']=countii
df.at[0,'3']=count3
df.at[0,'-3']=countiii
df.at[0,'4']=count4
df.at[0,'-4']=countiv
df.at[1,'']="User Input"
if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octant_range_names(mod)
df.to_excel('octant_outputsample.xlsx', index=False)  

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
