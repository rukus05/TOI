import pandas as pd
import time
import numpy as np
import re
import tkinter as tk
from tkinter import filedialog as fd
from definitions import coa_dict as coa
from definitions import hdc_list as hdcl
from definitions import roll_up_accts as rollup
from definitions import remove_acct_list as remove_accts
from definitions import credit_acct_list as cr_accts
from definitions import credit_rollup_accts as credit_rollups
from definitions import locations_dict as ld
#from definitions import baseline_accounts as baseline


def main():
    
    start = time.time()
    # If the raw data file has all the data in one file (002, 007, 008 sheets), you must save each entity in it's own file and run the program against each.
    # Read in Data from the "RawData.xlsx" file.
    f = FilePrompt()
    df = pd.read_excel(f)

    df = df.reset_index()
    # Fill all blank cells with zeros.  
    # It's critiacal that any columns you do calculations do not have blanks.
    df.fillna(0, inplace=True)

    df_groupby = df.groupby(['Batch Number', 'Home Department Code', 'Location Description', 'Pay Date'])

    for groupings,row in df_groupby:
        
        if groupings[1] not in hdcl:
            print (f'"{groupings[1]}" not in Home Department Code List')
        else:
            print (f'"{groupings[1]}" is in Home Department Code List')

        
 
    runningtime = time.time() - start

    # Start the "Save As" dialog box.
    #app = tk.Tk()
    #app.title("Save File As")
    #status_label = tk.Label(app, text="", fg="green")
    #status_label.pack()
    #save_button = tk.Button(app, text="Save as", command=save_dataframe(df_Output, status_label))
    #save_button.pack(padx=20, pady=10)
   
    
    print("The execution time is:", runningtime)


def FilePrompt():
    root = tk.Tk()
    root.title('Tkinter Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')
    root.withdraw()


    filename = fd.askopenfilename()

    return filename

    
def save_dataframe(df, sl):
    file_path = fd.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    
    if file_path:
        try:
            # Assuming df is your DataFrame
            df.to_excel(file_path, index=False)
            sl.config(text=f"Saved as {file_path}")
        except Exception as e:
            sl.config(text=f"Error: {str(e)}")


if __name__ == "__main__":
    main()