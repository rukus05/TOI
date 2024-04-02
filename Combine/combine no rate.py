import pandas as pd
import time
import tkinter as tk
import numpy as np
import re
from fns import FilePrompt
from fns import save_dataframe



def main():
    
    start = time.time()

    # These few lines prompt the user to select the files.
    print("Select the  PTO Liability file for the first month.")
    first_file = FilePrompt()

    df_first = pd.read_excel(first_file)
    df_first = df_first.reset_index()
    df_first.fillna(0, inplace=True)


    print("Select the PTO Liability file for the second month.")
    second_file = FilePrompt()

    df_second = pd.read_excel(second_file)
    df_second = df_second.reset_index()
    df_second.fillna(0, inplace=True)

    print("Select the Employee data file for the second month.")
    emp_file = FilePrompt()

    df_empdata = pd.read_excel(emp_file)
    df_empdata = df_empdata.reset_index()
    df_empdata.fillna(0, inplace=True)

    ### This line finds all the unique instances of of 'Employee' in the old file
    #unique_old_names = df_prior['Employee'].unique()
    #unique_current_names = df_current['Employee'].unique()

    # Combine all unique Postition IDs.

    df_first = df_first.dropna(axis = 1, how ='all')
    df_second = df_second.dropna(axis = 1, how = 'all')
    pids = pd.concat([df_first['Position ID'], df_second['Position ID']], ignore_index=True)
    print(type(pids))

    # Add the unique IDs to a dictionary
    pids_dict = {value: {'First Month' : 0, 'Second Month' : 0, 'Company' : None, 'Department' : None, \
                         'Location' : None, 'Location Code' : None} for value in pids}

    #print(pids_dict)

    # Create new Dataframe for the Output.
    df_Output = pd.DataFrame(columns=['Company', 'Position ID', 'Department', 'Location', 'Location Code', \
                                      'First Month Liability', 'Second Month Liablity', 'Second Month Expense'])

    for index, row in df_first.iterrows():
        if row['Position ID'] in pids_dict:
            pids_dict[row['Position ID']]['First Month'] = row['Sum of Liability']
        else:
            print(row['Position ID'] + ' from First Month file is not in dictionary.')
    
    for index, row in df_second.iterrows():
        if row['Position ID'] in pids_dict:
            pids_dict[row['Position ID']]['Second Month'] = row['Sum of Liability']
        else:
            print(row['Position ID'] + ' from Second Month file is not in dictionary.')
    

    #print(pids_dict)
    
    for index, row in df_empdata.iterrows():
        if row['Position ID'] in pids_dict:
            pids_dict[row['Position ID']]['Company'] = row['Company Code']
            pids_dict[row['Position ID']]['Department'] = row['Home Department Description']
            pids_dict[row['Position ID']]['Location'] = row['Location Description']
            pids_dict[row['Position ID']]['Location Code'] = row['Home Department Code']
        else:
            print(row['Position ID'] + ' is in Employee Data file but not in input files.')

    for key, value in pids_dict.items():
        df_Output.loc[len(df_Output.index)] = [pids_dict[key]['Company'], key, pids_dict[key]['Department'], \
                                               pids_dict[key]['Location'], pids_dict[key]['Location Code'], \
                                               pids_dict[key]['First Month'], pids_dict[key]['Second Month'], \
                                               pids_dict[key]['Second Month'] - pids_dict[key]['First Month']]
    

    app = tk.Tk()
    app.title("Save File As")
    status_label = tk.Label(app, text="", fg="green")
    status_label.pack()
    save_button = tk.Button(app, text="Save as", command=save_dataframe(df_Output, status_label))
    save_button.pack(padx=20, pady=10)
    # End calculation of Runtime
    runningtime = time.time() - start
    print("The execution time is:", runningtime)


if __name__ == "__main__":
    main()