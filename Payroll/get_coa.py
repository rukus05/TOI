import pandas as pd
import time
import math
import numpy as np
import json
from pprint import pprint
import re
import tkinter as tk
from tkinter import filedialog as fd

#from definitions import baseline_accounts as baseline


def getCOA(df):
    '''
    start = time.time()
    # If the raw data file has all the data in one file (002, 007, 008 sheets), you must save each entity in it's own file and run the program against each.
    # Read in Data from the "RawData.xlsx" file.
    f = FilePrompt()
    df = pd.read_excel(f)

    df = df.reset_index()
    # Fill all blank cells with zeros.  
    # It's critiacal that any columns you do calculations do not have blanks.
    df.fillna(0, inplace=True)
    '''
    

    # Convert the DataFrame to a dictionary where keys are from the first column, and values are lists of row values
    ed = df.set_index("Home Department Code").to_dict("index")
    # Use list comprehension to remove decimal points from the dictionary
    for k1, v1 in ed.items(): 
        ed[k1] = {k: int(v) for k, v in v1.items()}
        #for k2, v2 in v1.items():
        #    v1[k2] = {k: int(v) for k, v in v2.items()}
    
    return ed
    #updated_dict = {}
    #for k, v in excel_dict.items():
    #    updated_dict[k] = v[1:]
    #updated_dict = {key: value[1:] for key, value in excel_dict.items()}
    # Print the resulting dictionary
    #print(updated_dict)

    '''
    all_col_headers = list(df.columns)   
    #print(all_col_headers)
    # Remove the columns not used in the JE's
    # result_list = [x for x in original_list if x not in elements_to_remove]
    col_headers = [x for x in all_col_headers if x not in remove_accts]
   
    no_of_columns = len(col_headers)    
    
    # Remember:  Index is at 0, then first column, second column, etc, etc.  To get last Column, subtract 1
    # Like this:  print(col_headers[no_of_columns - 1])  
    
    # Reduce the size of the col_headers list to start with the Columns we want.  In this case, "Regular Earnings Total"
    RET = "Regular Earnings Total"
    if RET in col_headers:
        # Find index for element of "Regular Earnings Total"
        index_ret = col_headers.index(RET)

    # Create a new list that starts with the "Regular Earnings Total" header.
    money_headers = col_headers[index_ret:]
    # Discount for the last column, which is "Batch Number"
    money_headers.pop()
    #print(money_headers)
    # Save the number of money headers.
    size_of_money_headers = len(money_headers)
    #print(size_of_money_headers)

    
    for item in money_headers:
        #print(money_headers)
        if item not in coa:
            print(f'"{item}" not in COA')
        
    '''
    runningtime = time.time() - start

    output_file_path = 'COA_Dict.py'

    # Write the dictionary to the text file
    with open(output_file_path, 'w') as file:
        file.write(str(ed))
        #pprint(excel_dict, stream=file)
    file.close
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