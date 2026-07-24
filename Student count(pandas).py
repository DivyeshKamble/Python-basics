#! D:\Coding\env1\Scripts\python.exe
import pandas as pd
import numpy as np
'''#To find total no of students in stream''' 
c11 = pd.Series (data= [60 , 80 , 20] , index= ["Science","Commerce","Humanities"])
c12 = pd.Series (data= [50 , 70 , 30] , index= ["Science","Commerce", "Humanities"])
c1 = c11+c12
print ("Total students in class 11 and 12 are " )
print (c1)
