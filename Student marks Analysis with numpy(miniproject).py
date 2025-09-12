#!/usr/bin/env python
# coding: utf-8

# Student Marks Analysis with NumPy

# In[1]:


import numpy as np


# In[43]:


student_name = ["Palak","Kartik","Athira","Anshika","Priya","Koro","Shivram","Yash","Shivam","Pratham","Anjali","Poorvi"]
# C programing, Python, Java
sub = ["C Programing","Python Programming","Java Programing"]
marks = np.array([ 
    [99,67,89],
    [67,56,35],
    [56,76,43],
    [65,34,76],
    [67,87,54],
    [56,43,76],
    [66,34,87],
    [67,56,76],
    [76,78,80],
    [89,90,65],
    [67,78,89],
    [65,76,87]
])


# In[78]:


print("Data Analysis")
"""
for i in range(0,len(student_name)):
    print(f"{student_name[i]}: {marks[i]}")"""
total = marks.sum(axis=1)
avg_per_stu = marks.mean(axis=1)
avg_per_sub = marks.mean(axis=0)
sub_highest = marks.max(axis=0)
print("==Student Analysis==")
for i in range(0,len(student_name)):
    print(f"Total Marks of {student_name[i]} is {total[i]}")
    print(f"Average Marks of {student_name[i]} is {np.round(avg_per_stu[i],1)}")
    print("------------")
print("==Subject Analysis==")
for i in range(0,len(sub)):
    print(f"Average marks of {sub[i]} is {np.round(avg_per_sub,1)[i]}")
    print(f"Highest marks of {sub[i]} is {sub_highest[i]}")
    print("------------")

print(f"Highest and lowest Marks Overall: Highest={marks.max()} Lowest={marks.min()}")
for i in range(0,len(student_name)):
    if total[i] == total.max():
        print(f"Topper is {student_name[i]} with {total[i]} marks.")
print("\n==Subject Topper==")
for j in range(len(sub)):
    topper_index = np.argmax(marks[:, j]) 
    print(f"{sub[j]} Topper: {student_name[topper_index]} with {sub_highest[j]} marks")


# In[83]:


"""4. Extra Features (Optional)
If you want to make it stronger:
Count how many students passed/failed per subject.
Assign grades (A, B, C, etc.) based on averages.
Compare overall class performance (mean, median, standard deviation)."""
for i in range(0,len(avg_per_stu)):
    if avg_per_stu[i]>80:
        print(f"{student_name[i]} got A grade.")
    elif avg_per_stu[i]>60:
        print(f"{student_name[i]} got B grade.")
    elif avg_per_stu[i]>45:
        print(f"{student_name[i]} got C grade.")
    else:
        print(f"{student_name[i]} got D grade.")
    print("_____")
print("==Over all class performance==")
print(f"Mean of all student in class: {marks.mean():.2f}")
print(f"Median of all student in class: {np.median(marks):.2f}")
print(f"Standrad deviation of whole class: {np.std(marks):.2f}")


# In[93]:


def result(name):
    for i in range(0,len(student_name)):
        if student_name[i]==name:
            print("------------")
            if avg_per_stu[i]>80:
                print(f"{student_name[i]} got A grade.")
            elif avg_per_stu[i]>60:
                print(f"{student_name[i]} got B grade.")
            elif avg_per_stu[i]>45:
                print(f"{student_name[i]} got C grade.")
            else:
                print(f"{student_name[i]} got D grade.")
            print("......")
            for j, subject in enumerate(sub):
                print(f"{subject} marks is {marks[i][j]}")
            print(".....")
            print(f"Total Marks of {student_name[i]} is {total[i]}")
            print(f"Average Marks of {student_name[i]} is {np.round(avg_per_stu[i],1)}")
            
            print("------------")
name = input("Enter name you want to see marks details: ")
result(name)


# In[ ]:




