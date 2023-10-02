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


def main(): 
    
    start = time.time()
    # If the raw data file has all the data in one file (002, 007, 008 sheets), you must save each entity in it's own file and run the program against each.
    # Read in Data from the "RawData.xlsx" file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)

    df_toi = df_toi.reset_index()
    col_headers = df_toi.head()

    col_headers

    #df_groupby = df_toi.groupby(['Company Code', 'Home Department Code'])
    #print(df_groupby)





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