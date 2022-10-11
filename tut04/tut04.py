from ctypes import sizeof
from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0

def octant_longest_subsequence_count_with_range():
     #printing octant values
    for i,x in enumerate([1,-1,2,-2,3,-3,4,-4]):
        df.at[i,'octant']=x
    
    #initialized variables for getting row number
    c1=0
    l1=0
    c2=0
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
        x=0 
        list=[]
        for i in range(len(df['Octant'])):
            if df['Octant'][i]==octval:
                count+=1

                #when the count becomes equal to maximum value obtained previously, subsequent count is increased
                if(count==maxi):     
                    Subsequence_count+=1

                    # when count becomes equal to longest subsequence value, the index is added to list
                    list.append(i)
            else:
                count=0
        # Printing the values in coloumns of excel
        df.at[j,'Longest Subsequence Length']=maxi
        df.at[j,'Count']=Subsequence_count

        # printing octant values in Octant_2 column and string Time
        df.at[c1,'Octant_2']=octval
        c1+=1
        df.at[c1,'Octant_2']='Time'

        # increasing c1 by total number of subsequence count to match the given format 
        for i in range(Subsequence_count+1):
            c1+=1
        
        # printing longest subsequence value in the column
        df.at[l1,'Longest Subsequence Length 2']=maxi
        l1+=1
        df.at[l1,'Longest Subsequence Length 2']='From'
        l1+=1

        # printing the From time range for all the longest subsequence using the help of list of longest subsequence created before
        for i in range(len(list)):
            df.at[l1,'Longest Subsequence Length 2']=df['Time'][list[i]+1-maxi]
            l1+=1
        df.at[c2,'Count_2']=Subsequence_count
        c2+=1
        df.at[c2,'Count_2']='To'
        c2+=1

        # printing the To time for all the longest subsequence using the help of list of longest subsequence created before
        for i in range(len(list)):
            df.at[c2,'Count_2']=df['Time'][list[i]]
            c2+=1




from platform import python_version
ver = python_version()
from platform import python_version
try:
    import pandas as pd
    ver = python_version()
    try:  
        #Reading the input csv file
        df = pd.read_excel("input_octant_longest_subsequence_with_range.xlsx")

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

        # initialising coloumns
        df['octant']=''
        df['Longest Subsequence Length']=''
        df['Count']=''
        df['  ']=''
        df['Octant_2']=''
        df['Longest Subsequence Length 2']=''
        df['Count_2']=''

        # function call
        octant_longest_subsequence_count_with_range()

        df.to_excel('output.xlsx', index=False)  
    except FileNotFoundError:
        print("Not able to open the file. Try later")
    #This shall be the last lines of the code.
    if ver == "3.8.10":
        print("Correct Version Installed")
    else:
        print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
    #This shall be the last lines of the code.
    end_time = datetime.now()
    print('Duration of Program Execution: {}'.format(end_time - start_time))
except ImportError:
    print("Not found module Pandas")
