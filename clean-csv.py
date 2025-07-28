#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[10]:


def clean_csv(input_csv,output_csv):

    try:
        df = pd.read_csv(input_csv)
        print("file loaded successfully...........")
    except Exception as e:
        print(f"Error in loading file:{e}")
        return

    print("\n******Info of Data in File*********")
    print(df.info())

    df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
    print("\n******Standard column names********")

    print("\n********Handle missing value*********")
    print(df.isnull().sum())

    for col in df.columns:
        if df[col].dtype=="object":
            df[col]=df[col].fillna("Unknown")
        else:
            df[col]=df[col].fillna(0)
    print("Filled missing value")

    print("\n********date format*********")
    for col in df.columns:
        if 'date' in col:
            df[col] = pd.to_datetime(df[col],errors = 'coerce')
        elif df[col].dtype == 'object':
            try:
                df[col] = pd.to_numeric(df[col])
            except:
                pass
    print("****data formating is done****")

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"Removed {before-after} duplicates rows.")

    try:
        df.to_csv(output_csv,index = False)
        print(f"\n Cleaned data saved to '{output_csv}'")
    except Exception as e:
        print(f"error saving file: {e}")


# In[ ]:





# In[12]:


input_csv = r"C:\Users\Admin\Downloads\archive\dino_actions_tactical_630k.csv"
output_csv =r"C:\Users\Admin\Downloads\archive\dino_actions_tactical_630k-cleaned.csv"

clean_csv(input_csv,output_csv)


# In[ ]:




