import time
from pprint import pprint
import tkinter as tk
from COA_Dict import ed
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

    for k1, v1 in ed.items(): 
        for k2, v2 in v1.items():
            if isinstance(v2, (float, int)):
                v2 = int(v2)
    
    print(ed)
    
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