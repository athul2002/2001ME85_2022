from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0

# function definition
def octant_longest_subsequence_count():

    #printing octant values
    for i,x in enumerate([1,-1,2,-2,3,-3,4,-4]):
        df.at[i,'octant']=x
    
    #finding longest subsequence and count of longest subsequence 
    for j,octval in enumerate([1,-1,2,-2,3,-3,4,-4]):
        count=0
        maxi=0
        Subsequence_count=0

        #when the octant value in coloumn of Octant becomes equal 
        #to that of octant value obtained through enumeration the count is increased
        for i in range(len(df['Octant'])):
            if df['Octant'][i]==octval:
                count+=1

                #Maximum value is updated when the count becomes greater than current maximum value.
                maxi=max(count,maxi)
            else:
                count=0
        count=0

        #finding count of longest subsequence
        for i in range(len(df['Octant'])):
            if df['Octant'][i]==octval:
                count+=1

                #when the count becomes equal to maximum value obtained previously, subsequent count is increased
                if(count==maxi):
                    Subsequence_count+=1
            else:
                count=0
        
        # Printing the values in coloumns of excel
        try:
            df.at[j,'Longest Subsequence Length']=maxi
            df.at[j,'Count']=Subsequence_count
        except:
            print("An error occured while printing Longest subsequence / Count ")
            break
from platform import python_version
try:
    import pandas as pd
    ver = python_version()

    try:
            
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
        df['Longest Subsequence Length']=''
        df['Count']=''
        if ver == "3.8.10":
            print("Correct Version Installed")
        else:
            print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
        octant_longest_subsequence_count()
        df.to_excel('output_octant_longest_subsequence.xlsx', index=False)  
    except FileNotFoundError:
        print("Not able to open the file. Try later")
    #This shall be the last lines of the code.
    end_time = datetime.now()
    print('Duration of Program Execution: {}'.format(end_time - start_time))
except ImportError:
    print("Not found module Pandas")
