#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect('To_do_list.db')
cursor = conn.cursor()


# In[2]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
id INTEGER PRIMARY KEY AUTOINCREMENt,
name TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
)
''')
conn.commit()
print("Table created successfully............")


# In[3]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS task(
id INTEGER PRIMARY KEY AUTOINCREMENT,
task_name TEXT,
status TEXT
)
''')
conn.commit()
print("Table successfully created.................")


# In[4]:


def sign_up():
    name = input("YOUR NAME:")
    password = getpass.getpass("PASSWORD for easy future access:")

    try:
        cursor.execute("INSERT INTO user(name,password) VALUES (?,?)",(name,password))
        conn.commit()
        print("SIGN-UP IS DONE✅\n CONGO🤩")
    except:
        print("ERROR")


# In[ ]:





# In[5]:


def login():
    global current_user
    name = input("YOUR NAME:")
    password = getpass.getpass("YOUR PASSWORD:")

    cursor.execute("SELECT * FROM user WHERE name=? AND password=?",(name,password))
    user = cursor.fetchone()

    if user:
        print(f"WELCOME {user[1]}.........")
        return user
    else:
        print("❌Invalid account number or pin||||||||||||||||||||||")


# In[6]:


def add_task():
    task_name = input("Write TASK to add in To-do-list: ")
    cursor.execute("INSERT INTO task(task_name) VALUES (?)",(task_name,))
    conn.commit()
    print("Task is added👍👍...........")


# In[7]:


def view_tasks():
    cursor.execute("SELECT * FROM task")
    
    rows = cursor.fetchall()

    for i in rows:
        print(i)


# In[8]:


def mark_complete():
    task_id = input("Enter task ID to mark as complete: ")
    cursor.execute("UPDATE task SET status = 'DONE✅' WHERE id = ?",(task_id,))
    conn.commit()
    print("Task marked as complete..............")


# In[ ]:





# In[9]:


def dlt_task():
    task_name = input("ENTER TASK YOU WANT TO DELETE: ")
    cursor.execute("DELETE FROM task WHERE task_name = ?",(task_name,))

    conn.commit()
    print("Task is deleted successfully...........")
   


# In[10]:


def menu():
    print("********************* TO DO LISt ********************")
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. UPDATE TASK")
    print("4. DELETE TASK")
    print("5. LOGOUT👋")

    


# In[ ]:





# In[11]:


while True:
    print("___________ WELCOME TO TO-DO-LIST")
    print("1. SIGN-UP")
    print("2. LOGIN")
    print("3. EXIT")
    
    ch = input("Choose according to yourself😊: ")

    if ch == '1':
        sign_up()
    elif ch == '2':
        current_user = login()
        if current_user:
            while True:
                menu()
                chh = input("CHoose: ")
                if chh == '1':
                    add_task()
                elif chh == '2':
                    view_tasks()
                elif chh == '3':
                    mark_complete()
                elif chh == '4':
                    dlt_task()
                elif chh == '5':
                    print("++++++++++++LOGOUT++++++++++++++")
                    current_user=None
                    break
                else:
                    print("INVALID CHOICE😢")
    elif ch == '3':
        print("________THANKS FOR VISITING___________________")
        break
    else:
        print("Invalid choice😢")
conn.commit()


# In[ ]:





# In[ ]:




