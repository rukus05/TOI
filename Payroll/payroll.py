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


def main():
    
    start = time.time()
    # If the raw data file has all the data in one file (002, 007, 008 sheets), you must save each entity in it's own file and run the program against each.
    # Read in Data from the "RawData.xlsx" file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)

    df_toi = df_toi.reset_index()
    # Fill all blank cells with zeros.  
    # It's critiacal that any columns you do calculations do not have blanks.
    df_toi.fillna(0, inplace=True)
    # Put column headers into a List
    all_col_headers = list(df_toi.columns)   

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
    # Save the number of money headers.
    size_of_money_headers = len(money_headers)
        
    # Convert the Pay Date column to a datetime data type
    df_toi['Pay Date'] = pd.to_datetime(df_toi['Pay Date'])
    # Remove the hours, minutes, and seconds
    df_toi['Pay Date'] = df_toi['Pay Date'].dt.date

    # Group the Data Frame by Company Code,  Home Department Code, and Location.
    df_groupby = df_toi.groupby(['Company Code', 'Home Department Code', 'Location Description', 'Pay Date'])
    
    
    # Create a list the size of the columns of interest, "money_headers"
    values_list = [0 for _ in range(size_of_money_headers)]
    
    # Create new Dataframe for the Output.
    df_Output = pd.DataFrame(columns=['Pay Date', 'Account Number', 'Description', 'Debit Amount', 'Credit Amount', 'Location', 'Dept'])
    
    for groupings, row in df_groupby:
        # Find out what Home Department Code this row is, and get the index from the Home Department Code List
        if groupings[1] in hdcl:
            hdc_index = hdcl.index(groupings[1])
        # Use the Home Department Code Index to get the right GL's from the Chart of Accounts

        # Dictionary Defining the Roll up Accounts, and initialize sum amd G/L for each to 0.  
        rollupsums = {
            "Wages" : [0, 0], "401K Payable" : [0, 0], "Bonus-B_Bonus" : [0, 0], "FICA" : [0, 0], "Garnishments" : [0, 0], "HSA_Deduction" : [0, 0], "Medical Ins Ded" : [0, 0], \
            "Net Pay" : [0, 0], "Other Payroll Taxes" : [0, 0], "Overtime" : [0, 0], "Physician Bonus" : [0, 0], "Severance Expense" : [0, 0], "Tax Deduction" : [0, 0]
        }

        for i in range(size_of_money_headers):
            found = False
            lookupkey = ""
            for key, value_list in rollup.items():
                if i in value_list:
                    found = True
                    lookupkey = key
                    break
            # If this payroll item was found above, and the COA is not empty for it, then execute.      
            if found and (i in coa and coa[i]):
                rollupsums[lookupkey][0] += row[money_headers[i]].sum()
                rollupsums[lookupkey][1] = coa[i][hdc_index]
                
            else:    
                values_list[i] = row[money_headers[i]].sum()
                if values_list[i] != 0:
                    if coa[i]:
                       
                        # Convert data type to datetime64[ns]
                        ped = groupings[3]
                        
                        # Clean up Batch Number text
                        text = str(row['Batch Number'])
                        keyword = "Name"
                        parts = text.split(keyword)
                        if len(parts) > 1:
                            truncated_text = parts[0]
                        else:
                            truncated_text = text

                        #print(ld[groupings[2]])
                        
                        # If matches for credit accounts, else it's a debit account.  Values are printed in appropriate column. 
                        # To address leading or trailing spaces in Location Descriptions, strip() method had to be employed whereever groupings[2] of the groupby object was referenced.
                        if i in cr_accts:
                            df_Output.loc[len(df_Output.index)] = [ped, coa[i][hdc_index], groupings[0] + ' ' + truncated_text + ' ' + str(money_headers[i]), "", values_list[i], ld[groupings[2].strip()], hdcl[hdc_index]]
                        else:
                            df_Output.loc[len(df_Output.index)] = [ped, coa[i][hdc_index], groupings[0] + ' ' + truncated_text + ' ' + str(money_headers[i]), values_list[i], "", ld[groupings[2].strip()], hdcl[hdc_index]]
        
        for acct, z in rollupsums.items():
            if z[0] != 0:
                ped = groupings[3]
                
                # Clean up Batch Number text
                text = str(row['Batch Number'])
                keyword = "Name"
                parts = text.split(keyword)
                if len(parts) > 1:
                    truncated_text = parts[0]
                else:
                    truncated_text = text

                # If matches for credit accounts, else it's a debit account
                if acct in credit_rollups:
                    df_Output.loc[len(df_Output.index)] = [ped, z[1], groupings[0] + ' ' + truncated_text + ' ' + acct, "", z[0], ld[groupings[2].strip()], hdcl[hdc_index]]
                else:
                    df_Output.loc[len(df_Output.index)] = [ped, z[1], groupings[0] + ' ' + truncated_text + ' ' + acct, z[0], "", ld[groupings[2].strip()], hdcl[hdc_index]]
            
 
    
    # Start the "Save As" dialog box.
    app = tk.Tk()
    app.title("Save File As")
    status_label = tk.Label(app, text="", fg="green")
    status_label.pack()
    save_button = tk.Button(app, text="Save as", command=save_dataframe(df_Output, status_label))
    save_button.pack(padx=20, pady=10)
   
    runningtime = time.time() - start
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