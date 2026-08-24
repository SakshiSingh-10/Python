import numpy as np
import pandas as pd


sallery=np.array([
    [25000,2,80],
    [45000,5,90],
    [30000,3,75],
    [60000,8,95],
    [35000,4,85]
])
Salary=["salary" "Experience (Years)"  ,"Performance Score"]

avrage= np.mean(sallery[:,0])
heighestS= np.max(sallery[:,0])
lowestS=np.min(sallery[:,0])
avrage_experiance=np.mean(sallery[:1])
above=np.where(sallery[:,0]>40000)
above_performance=sallery[sallery[:,2]>80]
heighestS_score_index=np.argmax(sallery[:2])
standerd= np.std(sallery[:0])
sallery_status=np.where(sallery[:,0]>40000,
"High Sallery","Low Sallery")            
df=pd.DataFrame(sallery,
    columns=["Sallery","Experiance","Performance"])
df["Salary Status"]=sallery_status
print (df)   

print("Average Sallery",avrage)
print("Height Sallery",heighestS)
print("Lowest Sallery",lowestS)
print("Avreage Experiance",avrage_experiance)

print("\nEmployees with salary > 40000:")
print(above)

print("\n\nEmployees with performance > 80:")
print(above_performance)

print("\nHighest Performance Employee:")
print(heighestS_score_index)

print("\nSalary Standard Deviation:")
print(standerd)

print("\n Final Data Frame:")
print(df)
       