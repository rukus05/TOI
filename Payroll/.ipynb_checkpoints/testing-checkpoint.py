import pandas as pd
import time
import re
import openpyxl
import datetime
import tkinter as tk
from tkinter import TOP, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfile
from toicoa import coa_dict as coa


def main(): 
    
    start = time.time()
    # If the raw data file has all the data in one file (002, 007, 008 sheets), you must save each entity in it's own file and run the program against each.
    # Read in Data from the "RawData.xlsx" file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)

    df_toi = df_toi.reset_index()
    col_headers = list(df_toi.columns)          #Put column headers into a List
    #col_headers = df_toi.columns
    no_of_columns = len(col_headers)            #Remember:  Index is at 0, then first column ... second column ... etc, etc.  To get last Column, subtract 1
                                                # Like this:  print(col_headers[no_of_columns - 1])
    print(no_of_columns)
    
    #print(col_headers)
    

    #df_groupby = df_toi.groupby(['Company Code', 'Home Department Code'])
    #print(df_groupby)

    print(coa)





def FilePrompt():
    root = tk.Tk()
    root.title('Tkinter Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')
    root.withdraw()


    filename = fd.askopenfilename()

    return filename

if __name__ == "__main__":
    main()