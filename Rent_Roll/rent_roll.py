from zpack.fns import FilePrompt
from zpack.fns import save_dataframe
import tkinter as tk
import pandas as pd
import time


def main():

    start = time.time()
    # Select input (Raw data) file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)
    df_toi = df_toi.reset_index()

    gl_code = {'Rent' : 14010, 'Rent Sales Tax' : 14020, 'CAM' : 14020, 'CAM Sales Tax' : 14020, 'CPI' : 14010}

    header_list = ['Rent', 'Rent Sales Tax', 'CAM', 'CAM Sales Tax', 'CPI']
    # Create new Dataframe for the Output.
    df_Output = pd.DataFrame(columns=['Vendor ID', 'Description', 'DR', 'CTT#', 'Location', 'Line'])

    for index,row in df_toi.iterrows():
        l_counter = 0
        for h in header_list:
            
            if row[h] != 0:
                l_counter = l_counter + 1
                df_Output.loc[len(df_Output.index)] = [row['Sage Vendor ID'], h, row[h], gl_code[h], row['Clinic #'], l_counter]
    




    # Start the "Save As" dialog box.
    app = tk.Tk()
    app.title("Save File As")
    status_label = tk.Label(app, text="", fg="green")
    status_label.pack()
    save_button = tk.Button(app, text="Save as", command=save_dataframe(df_Output, status_label))
    save_button.pack(padx=20, pady=10)
   
    runningtime = time.time() - start
    print("The execution time is:", runningtime)





if __name__ == "__main__":
    main()
