import pandas as pd
import time
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
    pids = pd.concat([df_first['Position ID'], df_second['Position ID']], ignore_index=True)

    # Add the unique IDs to a dictionary
    pids_dict = {value: None for value in pids}

    print(pids_dict)

if __name__ == "__main__":
    main()