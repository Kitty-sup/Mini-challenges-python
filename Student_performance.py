#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


conn = sqlite3.connect('student_performance.db')
cursor = conn.cursor()


# In[3]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    class TEXT
    )
''')
conn.commit()
print("Table created")


# In[4]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS marks (
    mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT,
    marks INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
''')
conn.commit()
print("New marks table created!")


# In[ ]:





# In[5]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS attendance(
    atd_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    total_days INTEGER,
    present_days INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
    )
''')
conn.commit()
print("Table created")


# In[6]:


def add_student(name,stu_class):
    cursor.execute("INSERT into students(name,class) VALUES (?,?)",(name,stu_class))
    conn.commit()
    print("Student added in a table...........")


# In[7]:


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for i in rows:
        print(row)


# In[8]:


def update_student_name(stu_id,new_name):
    cursor.execute("UPDATE students set name=? where id=?",(stu_id,new_name))
    conn.commit()
    print("Name is updated...............")


# In[9]:


def dlt_student(stu_id):
    cursor.execute("delete from students where id = ?",(stu_id,))
    conn.commit()
    print("Student record is deleted.................")


# In[10]:


def add_marks(stu_id,sub,marks):
    cursor.execute("INSERT into marks(student_id,subject,marks) VALUES (?,?,?)",(stu_id,sub,marks))
    conn.commit()
    print("marks added in a table...........")


# In[11]:


def view_marks():
    cursor.execute("SELECT * FROM marks")
    rows = cursor.fetchall()
    for i in rows:
        print(row)


# In[12]:


def update_marks(mark_id,new_marks):
    cursor.execute("UPDATE marks set marks=? where student_id=?",(mark_id,new_marks))
    conn.commit()
    print("marks is updated...............")


# In[13]:


def dlt_marks(mark_id):
    cursor.execute("delete from marks where student_id = ?",(mark_id,))
    conn.commit()
    print("marks record is deleted.................")


# In[14]:


def add_atd(stu_id,total,present):
    cursor.execute("INSERT into attendance(student_id,total_days,present_days) VALUES (?,?,?)",(stu_id,total,present))
    conn.commit()
    print("attendance added in a table...........")


# In[15]:


def view_atd():
    cursor.execute("select * from attendance")
    rows = cursor.fetchall()
    for i in rows:
        print(rows)
    


# In[16]:


def update_atd(atd_id,new_total,new_present):
    cursor.execute("Update attendance set total_days=?,present_days=? where atd_id=?",(atd_id,new_total,new_present))
    conn.commit()
    print("attendance is updated...........")


# In[17]:


def dlt_atd(atd_id):
    cursor.execute("delete from attendance where atd_id=?",(atd_id,))
    conn.commit()
    print("Attendance is deleted..................")


# In[ ]:





# In[18]:


add_student("Palak", "10A")
add_student("Ankit", "10A")
add_student("Riya", "10B")
add_student("Ishaan", "10B")
add_student("Meera", "10A")


# In[19]:


# Palak
add_marks(1, "Math", 88)
add_marks(1, "Science", 92)
add_marks(1, "English", 85)

# Ankit
add_marks(2, "Math", 76)
add_marks(2, "Science", 81)
add_marks(2, "English", 78)

# Riya
add_marks(3, "Math", 91)
add_marks(3, "Science", 89)
add_marks(3, "English", 95)

# Ishaan
add_marks(4, "Math", 64)
add_marks(4, "Science", 70)
add_marks(4, "English", 68)

# Meera
add_marks(5, "Math", 85)
add_marks(5, "Science", 88)
add_marks(5, "English", 90)


# In[20]:


add_atd(1, 50, 45)  # Palak
add_atd(2, 50, 40)  # Ankit
add_atd(3, 50, 49)  # Riya
add_atd(4, 50, 35)  # Ishaan
add_atd(5, 50, 47)  # Meera


# In[21]:


student_df = pd.read_sql_query("SELECT * FROM students",conn)
marks_df = pd.read_sql_query("select * from marks",conn)
attendance_df = pd.read_sql_query("select * from attendance",conn)


# In[22]:


student_df.head(40)


# In[23]:


marks_df.head(21)


# In[24]:


attendance_df.head(10)


# In[25]:


dlt_student(1)


# In[26]:


avg_marks= marks_df.groupby("student_id")['marks'].mean().reset_index()
avg_marks.columns=['student_id','average_marks']
print(avg_marks)


# In[27]:


topper_df = marks_df.loc[marks_df.groupby('subject')['marks'].idxmax()]
print(topper_df[['subject','student_id','marks']])


# In[28]:


attendance_df['attendance_percent'] = np.round((attendance_df["present_days"]/attendance_df["total_days"])*100,2)
print(attendance_df[['student_id','attendance_percent']])


# In[29]:


avg_marks = marks_df.groupby("student_id")['marks'].mean().reset_index()

attendance_df['attendance_percent'] = np.round((attendance_df["present_days"]/attendance_df["total_days"])*100,2)

combined = pd.merge(avg_marks,attendance_df,on='student_id')
correlation = combined['marks'].corr(combined['attendance_percent'])
print(f"Correlation: {correlation:.2f}")


# In[30]:


subject_avg = marks_df.groupby("subject")['marks'].mean()

subject_avg.plot(kind ='bar', color = 'pink')


# In[31]:


student_id  = 1
student_marks = marks_df[marks_df['student_id']==student_id]

plt.plot(student_marks['subject'],student_marks['marks'], marker='o',linestyle='--',color='green')
plt.plot(0,100)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




