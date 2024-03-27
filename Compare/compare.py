import pandas as pd
import time
import numpy as np
import re
import tkinter as tk
from tkinter import filedialog as fd


def main():
    start = time.time()
    # These few lines prompt the user to select the files.
    print("Select the prior month file.")
    oldfile = FilePrompt()

    df_prior = pd.read_excel(oldfile)
    df_prior = df_prior.reset_index()

    print("Select the current month file.")
    newfile = FilePrompt()

    df_current = pd.read_excel(newfile)
    df_current = df_current.reset_index()

    # This line finds all the unique instances of of 'Employee' in the old file
    unique_old_names = df_prior['Employee'].unique()
    unique_current_names = df_current['Employee'].unique()







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