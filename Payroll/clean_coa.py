import time
import math
from pprint import pprint
import tkinter as tk
from COA_Dict import excel_dict as ed
from tkinter import filedialog as fd

#from definitions import baseline_accounts as baseline


def main():
    
   
   
    start = time.time()

    for k1, v1 in ed.items(): 
        for k2, v2 in v1.items():
            v2 = math.trunc(v2)
            print (v2)
    
    #print(ed)
    
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