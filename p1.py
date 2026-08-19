# project 1 
import numpy as np
import pandas as pd
marks=np.array([[85 , 80, 90],
                [70,75,65],
                [92,888,95],
                [60,72,68],
                [78,82,80]
    
])
subject = ["pyhton","sql","Machine Learning"]
total =np.sum(marks,axis=1)
average=np.mean(marks,axis=1)
subject_average=np.mean(marks,axis=0)
heighest=np.max(marks,axis=0)
lowest=np.min(marks,axis=0)
above=np.where(marks>80)[0]
status=np.where(average>=40,"pass","Fail")
heighest_student=np.argmax(average)
std=np.std(marks,axis=0)
df=pd.DataFrame(marks,columns=subject)
df["total"]=total
df["Avrage"]=average
df["status"]=status

print("result")
print(df)
print("avrage marks in each student")
print(subject_average)
print("heighest marks in each sub")
print(heighest)
print("lowest score in each subject")
print(lowest)
print("student with avrage above 80 marks")
print(above)
print("index of heighest performance ")
print(heighest_student)
print("standard derivation odf each student ")
print(std)