#Function defined
def octant_transition_count(mod=5000):
    range_list[-1]-=1

    #heading of coloumns
    Row_num=2+len(range_list)+2
    df.at[2+len(range_list)+2,'Octant ID']="Overall Transition Count"
    df.at[Row_num+1,'''1''']="To"
    df.at[Row_num+2,'Octant ID']="Count"
    df.at[Row_num+3,'']="From"
    
    #Octant values printing in row and column manner
    for i,x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
        df.at[Row_num+3+i,'Octant ID']=x
        df.at[Row_num+2,x]=x
    
    #dictionary for storing octant transition values
    Trans_count_dict = {
    1: {1: 0,-1: 0,2: 0,-2: 0,3: 0,-3: 0,4: 0,-4: 0},
    -1: {1: 0,-1: 0,2: 0,-2: 0,3: 0,-3: 0,4: 0,-4: 0},
    2: {1: 0,-1: 0,2: 0,-2: 0,3: 0,-3: 0,4: 0,-4: 0},
    -2: {1: 0,-1: 0,2: 0,-2: 0,3: 0,-3: 0,4: 0,-4: 0},
    3: {1: 0,-1: 0,2: 0,-2: 0,3: 0,-3: 0,4: 0,-4: 0},
    -3: {1: 0,-1: 0,2: 0,-2: 0,3: 0,-3: 0,4: 0,-4: 0},
    4: {1: 0,-1: 0,2: 0,-2: 0,3: 0,-3: 0,4: 0,-4: 0},
    -4: {1: 0,-1: 0,2: 0,-2: 0,3: 0,-3: 0,4: 0,-4: 0}
    }


    for num in range(len(range_list)-1):
        mod_row = Row_num+14+num*(14)
        mod_transitions_count = copy.deepcopy(Trans_count_dict)
        df.at[mod_row,'Octant ID'] = 'Mod Transition Count'
        df.at[mod_row + 1, 'Octant ID'] = str(range_list[num]) + '-' + str(range_list[num+1]-1)
        df.at[mod_row +2, 'Octant ID']="To"
        df.at[mod_row +3, 'Octant ID'] = "Count"
        for i,x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
            df.at[mod_row+3+i,'Octant ID']=x
            df.at[mod_row+3,x]=x
        df.at[mod_row + 3, ''] = "From"
        for i in range(range_list[num], range_list[num+1]):
            mod_transitions_count[df['Octant'][i+1]][df['Octant'][i]]+=1
    #mod transition count
        for i in mod_transitions_count:
            for idx, j in enumerate(mod_transitions_count[i]):
                df.at[mod_row+3+idx,str(i)]=mod_transitions_count[i][j] 
    #overall transition count
    for i in range(1, len(df['U'])):
        Trans_count_dict[df['Octant'][i]][df['Octant'][i-1]]+=1
    for i in Trans_count_dict:
        for idx, j in enumerate(Trans_count_dict[i]):
            df.at[Row_num+2+idx,str(i)]=Trans_count_dict[i][j]
            
#Function defined
def octact_identification(mod=5000):
    df.at[1,'Octant ID']="Mod "+str(mod)
#Created a list named range_list and added the range values in that
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
import copy 
#Reading the input csv file
df = pd.read_excel("input_octant_transition_identify.xlsx")

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
range_list=[0]
#function call
octact_identification(mod)
#Made output csv file named Octant_output.csv

ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octant_transition_count(mod)
df.to_excel('octant_output.xlsx', index=False)  
