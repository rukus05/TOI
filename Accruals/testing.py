import tkinter as tk
import pandas as pd
import time
import numpy as np
from fns import FilePrompt
from fns import save_dataframe
from definitions import locations_dict as ld


def main():

    start = time.time()
 
    # Select input (Raw data) file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)
    df_toi = df_toi.reset_index()


    df_toi['Posted dt.'] = pd.to_datetime(df_toi['Posted dt.'])

    df_toi['Month'] = df_toi['Posted dt.'].dt.to_period('M')

    unique_months = sorted(df_toi['Posted dt.'].dt.to_period('M').unique())
    # Extract out only the year and month of the date.
    #month_year_list = [dt.strftime("%Y-%m") for dt in unique_months]
    # Create a dictionary based on unique monts
    um_dict = []
    monthly_sums ={}
    for um in unique_months:
        um_dict.append(um)

    others = ['GL Code', 'Vendor', 'Location', 'Description', 'Accrual Amount']
    # Aggregate into a Headers list
    new_list = others + unique_months
    # Create an output dataframe based on the new list above
    df_Output = pd.DataFrame(columns = new_list)
    
    # Create a dictionary to hold the Monthly sums.
    monthly_sums = {}


    df_groupby = df_toi.groupby(['GL Code', 'Vendor', 'Location', 'Department'])


    for groupings, group_data in df_groupby:
        if groupings[1]:
            
            est_accrual = row['Amount'].mean()
            #df_groupby =df_groupby.a
            #location_code = ld[groupings[2].strip()]
            df_Output.loc[len(df_Output.index)] = [groupings[0], groupings[1], groupings[2], groupings[3], est_accrual]
            

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