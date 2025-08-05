#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import logging
import tkinter as tk
from tkinter import ttk,filedialog, messagebox



# In[70]:


def clean_csv(input_csv,output_csv,log_callback=None, return_df=False,low_memory=False):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    try:
        df = pd.read_csv(input_csv)
        log("file loaded successfully...........")
    except Exception as e:
        log(f"Error in loading file:{e}")
        return


    original_rows = len(df)
    missing_before = df.isnull().sum().sum()
    missing_per_column = df.isnull().sum()

    
    print("\n******Info of Data in File*********")
    print(df.info())

    df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
    log("\n******Standard column names********")

    log("\n********Handle missing value*********")
    print(df.isnull().sum())

    for col in df.columns:
        if df[col].dtype=="object":
            df[col]=df[col].fillna("Unknown")
        else:
            df[col]=df[col].fillna(0)
    log("Filled missing value")

    log("\n********date format*********")
    for col in df.columns:
        if 'date' in col:
            df[col] = pd.to_datetime(df[col],errors = 'coerce')
        elif df[col].dtype == 'object':
            try:
                df[col] = pd.to_numeric(df[col])
            except:
                pass
    log("****data formating is done****")

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    log(f"Removed {before-after} duplicates rows.")

    final_rows = len(df)

    log("\n😊SUMMARY REPORT")
    log(f"Rows before cleaning: {original_rows}")
    log(f"Rows after cleaning: {final_rows}")
    log(f"Duplicates rows removed: {original_rows-final_rows}")
    log(f"Total missing values: {missing_before}")
    log(f"Top columns with the most missing values before cleaning:")
    log( str(missing_per_column.sort_values(ascending=False).head()))

    try:
        df.to_csv(output_csv,index = False)
        log(f"\n Cleaned data saved to '{output_csv}'")
    except Exception as e:
        log(f"error saving file: {e}")
    if return_df:
        return df


    


# In[ ]:





# In[ ]:





# In[60]:


def browse_input():
    file_path = filedialog.askopenfilename(filetypes = [("CSV files","*.csv")])
    input_entry.delete(0,tk.END)
    input_entry.insert(0, file_path)
    


# In[61]:


def browse_ouput():
    file_path = filedialog.asksaveasfilename(defaultextension = ".csv",filetypes=[("CSV files","*.csv")])
    output_entry.delete(0,tk.END)
    output_entry.insert(0,file_path)


# In[62]:


def run_cleaner():
    input_file = input_entry.get()
    output_file = output_entry.get()
    log_box.delete(1.0,tk.END)

    if not input_file or not output_file:
        messagebox.showerror("Error","Please select both input and output files.")
        return
    clean_csv(input_file,output_file,log_callback = write_log)
    


# In[63]:


def write_log(message):
    log_box.insert(tk.END,message +"\n")
    log_box.see(tk.END)


# In[64]:


def show_preview(df, title = "Data Preview"):
    if df.empty or len(df.columns) == 0:
        messagebox.showwarning("no Data", "DataFrame is emptyor has no valid columns to display. ")
        return

    preview_window = tk.Toplevel()
    preview_window.title(title)
    preview_window.geometry("800x300")

    frame = tk.Frame(preview_window)
    frame.pack(expand=True, fill= "both")
    
    tree = ttk.Treeview(preview_window)
    tree.pack(expand=True, fill="both")

    vsb = ttk.Scrollbar(frame,orient="vertical", command=tree.yview)
    vsb.pack(side = "right", fill = "y")
    tree.configure(yscrollcommand=vsb.set)

    hsb = ttk.Scrollbar(frame,orient="horizontal", command=tree.xview)
    hsb.pack(side = "bottom", fill = "x")
    tree.configure(xscrollcommand=hsb.set)
    
    columns = [str(col) for col in df.columns]
    tree["columns"] = columns
    tree["show"] = "headings"

    for col in columns:
        tree.heading(col,text=col)
        tree.column(col,width=120)

    for _, row in df.head(10).iterrows():
        tree.insert("","end",values=[str(val) for val in row])


# In[65]:


def preview_original():
    input_file = input_entry.get()
    if not input_file:
        messagebox.showerror("Error","Please select an input file first.")
        return
    try:
        df = pd.read_csv(input_file)
        show_preview(df,"Original Data Preview")
    except Exception as e:
        messagebox.showerror("Error",f"Could not load file: {e}")


# In[66]:


def preview_cleaned():
    input_file = input_entry.get()
    output_file = output_entry.get()
    if not input_file or not output_file:
        messagebox.showerror("Error","Please select  both Input and Output files.")
        return
    try:
        df_cleaned = clean_csv(input_file, output_file, log_callback = write_log, return_df = True)
        show_preview(df_cleaned, "Cleaned Data Preview")
    except Exception as e:
        messagebox.showerror("Error",f"Could not clean or prview file : {e}")


# In[ ]:


window = tk.Tk()
window.title("CSV Cleaner ")
window.geometry("600x500")

tk.Label(window, text = "Select input csv file: ").pack(pady=5)
input_entry = tk.Entry(window, width = 60)
input_entry.pack()
tk.Button(window, text = "Browse", command = browse_input).pack(pady=5)

tk.Label(window, text = "Select cleaned  file as: ").pack(pady=5)
output_entry = tk.Entry(window, width = 60)
output_entry.pack()
tk.Button(window, text = "Browse", command = browse_ouput).pack(pady=5)

tk.Button(window, text = "Clean Csv", command = run_cleaner,bg = "green",fg = "White").pack(pady=10)

tk.Button(window, text = "Preview Original Data", command = preview_original).pack(pady = 5)
tk.Button(window, text = "Preview Cleaned Data", command = preview_cleaned).pack(pady = 5)
tk.Label(window, text="output log: ").pack()
log_box = tk.Text(window, height=15,width=70)
log_box.pack()

window.mainloop()


# In[ ]:





# In[ ]:




