import pandas as pd
import time
import re
import openpyxl
import datetime
import tkinter as tk
from tkinter import TOP, ttk
from tkinter import filedialog as fd
#from tkinter.messagebox import showinfo
#from tkinter.filedialog import asksaveasfile
from toicoa import coa_dict as coa




def main():
    
    start = time.time()
    # If the raw data file has all the data in one file (002, 007, 008 sheets), you must save each entity in it's own file and run the program against each.
    # Read in Data from the "RawData.xlsx" file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)

    df_toi = df_toi.reset_index()

    # Put column headers into a List
    col_headers = list(df_toi.columns)          
    
    no_of_columns = len(col_headers)          
    # Remember:  Index is at 0, then first column, second column, etc, etc.  To get last Column, subtract 1
    # Like this:  print(col_headers[no_of_columns - 1])  
    print(col_headers[no_of_columns - 1]) 

    #print(col_headers)

    #  This code would get the size of each group
    #df_groupby = df_toi.groupby(['Company Code', 'Home Department Code']).size()
    #df_groupby = df_groupby.reset_index()

    df_groupby = df_toi.groupby(['Company Code', 'Home Department Code'])
    result_df = df_groupby['Regular Earnings Total'].sum()
    result_df = result_df.reset_index()
    
    
    
    
    
    # Create a button to trigger the "Save As" dialog
    app = tk.Tk()
    app.title("Save File As")
    status_label = tk.Label(app, text="", fg="green")
    status_label.pack()
    save_button = tk.Button(app, text="Save as", command=save_dataframe(result_df, status_label))
    save_button.pack(padx=20, pady=10)

    

        


def FilePrompt():
    root = tk.Tk()
    root.title('Tkinter Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')
    root.withdraw()


    filename = fd.askopenfilename()

    return filename

    
def save_dataframe(df, sl):
    file_path = fd.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    
    if file_path:
        try:
            # Assuming df is your DataFrame
            df.to_excel(file_path, index=False)
            sl.config(text=f"Saved as {file_path}")
        except Exception as e:
            sl.config(text=f"Error: {str(e)}")


if __name__ == "__main__":
    main()