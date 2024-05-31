import tkinter as tk
import pandas as pd
import time
import numpy as np
from zpack.fns import FilePrompt
from zpack.fns import save_dataframe
from toi_module.definitions import locations_dict as ld
from toi_module.definitions import coa_accrual_dict as cd

# Input file format changed on 11/9/23 by Rosel.  (See Accruals.py file in archive for old format program)#

def main():

    start = time.time()
 
    # Select input (Raw data) file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)
    df_toi = df_toi.reset_index()

    # Create a dataframe for the output
    df_Output = pd.DataFrame(columns=['GL Code', 'GL Name', 'Vendor', 'Location', 'Department', 'Description', 'Accrual Amount'])
    
    # Account Code is GL Name; Supplier Name is Vendor;  Custom 5 - Code is Location;  Custom 3 - Code is Department
    df_groupby = df_toi.groupby(['Account Code', 'Supplier Name', 'Custom 5 - Code', 'Custom 3 - Code'])


    for groupings, row in df_groupby:
        est_accrual = row['Amount'].sum()
        #location_code = ld[groupings[2].strip()]
        df_Output.loc[len(df_Output.index)] = [cd[groupings[0]], groupings[0], groupings[1], groupings[2], groupings[3], row['Description'], est_accrual]
            
    runningtime = time.time() - start
    
    # Start the "Save As" dialog box.
    app = tk.Tk()
    app.title("Save File As")
    status_label = tk.Label(app, text="", fg="green")
    status_label.pack()
    save_button = tk.Button(app, text="Save as", command=save_dataframe(df_Output, status_label))
    save_button.pack(padx=20, pady=10)
   
    
    print("The execution time is:", runningtime)




if __name__ == "__main__":
    main()