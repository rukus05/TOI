import pandas as pd
import time
import numpy as np
import re
import tkinter as tk
from tkinter import filedialog as fd
from toi_module.definitions import (
    hdc_list as hdcl,
    roll_up_accts as rollup,
    remove_acct_list as remove_accts,
    credit_acct_list as cr_accts,
    credit_rollup_accts as credit_rollups,
    locations_dict as ld,
    duplicate_debits_dict as duplicate_debits
)
from zpack.fns import FilePrompt, save_dataframe
from get_coa import getCOA
#from definitions import baseline_accounts as baseline

def load_chart_of_accounts():
    """Load and process the Chart of Accounts file."""
    print('Select the latest Chart of Accounts file:')
    file_prompt = FilePrompt()
    df_coa = pd.read_excel(file_prompt)
    df_coa = df_coa.reset_index()
    df_coa.fillna(0, inplace=True)
    return getCOA(df_coa)

def load_payroll_data():
    """Load and process the payroll data file."""
    print('Select the raw data file to run Payroll for:')
    file_prompt = FilePrompt()
    df_toi = pd.read_excel(file_prompt)
    df_toi = df_toi.reset_index()
    return df_toi

def get_money_headers(df_toi):
    """Extract and process the money-related column headers."""
    all_col_headers = list(df_toi.columns)
    col_headers = [x for x in all_col_headers if x not in remove_accts]
    
    # Find the starting point for money headers
    ret_index = col_headers.index("Regular Earnings Total")
    money_headers = col_headers[ret_index:]
    
    # Remove unnecessary trailing columns
    while money_headers[-1] in ['Batch Number', 'Position ID']:
        money_headers.pop()
    
    return money_headers

def process_payroll_row(groupings, row, df_coa, money_headers):
    """Process a single payroll row and return the output entries."""
    homedeptcode = groupings[1]
    if homedeptcode not in hdcl:
        print(f"{homedeptcode} is not in the Home Dept Codes!")
        return []

    # Initialize rollup sums
    rollupsums = {
        "Wages": [0, 0], "401K Payable": [0, 0], "Bonus-B_Bonus": [0, 0],
        "FICA": [0, 0], "Garnishments": [0, 0], "HSA_Deduction": [0, 0],
        "Medical Ins Ded": [0, 0], "Net Pay": [0, 0], "Other Payroll Taxes": [0, 0],
        "Overtime": [0, 0], "Physician Bonus": [0, 0], "Severance Expense": [0, 0],
        "Tax Deduction": [0, 0]
    }

    output_entries = []
    values_list = [0] * len(money_headers)

    # Process each money header
    for counter, header in enumerate(money_headers):
        found = False
        lookupkey = ""
        
        # Check if header is in rollup accounts
        for key, value_list in rollup.items():
            if header in value_list:
                found = True
                lookupkey = key
                break

        if found and (header in df_coa and df_coa[header][homedeptcode] != 0):
            rollupsums[lookupkey][0] += row[header].sum()
            rollupsums[lookupkey][1] = df_coa[header][homedeptcode]
        else:
            values_list[counter] = abs(row[header].sum()) if header == 'PHA_Phone Allowance_Deduction' else row[header].sum()
            
            if values_list[counter] != 0 and df_coa[header][homedeptcode]:
                entry = create_output_entry(
                    groupings, header, values_list[counter],
                    df_coa[header][homedeptcode], homedeptcode
                )
                output_entries.extend(entry)

    # Process rollup sums
    for acct, (amount, gl_account) in rollupsums.items():
        if amount != 0:
            entry = create_output_entry(
                groupings, acct, amount, gl_account, homedeptcode,
                is_rollup=True
            )
            output_entries.extend(entry)

    return output_entries

def create_output_entry(groupings, description, amount, gl_account, homedeptcode, is_rollup=False):
    """Create output entries for a single transaction."""
    entries = []
    ped = groupings[3]
    batch_num = groupings[0]
    location = ld[groupings[2].strip()]
    
    if (is_rollup and description in credit_rollups) or (not is_rollup and description in cr_accts):
        entries.append([ped, gl_account, f"{batch_num} {description}", "", amount, location, homedeptcode])
    else:
        if description in duplicate_debits:
            entries.append([ped, gl_account, f"{batch_num} {description}", amount, "", location, homedeptcode])
            entries.append([ped, '14900', f"{batch_num} {description}", "", amount, location, homedeptcode])
        else:
            entries.append([ped, gl_account, f"{batch_num} {description}", amount, "", location, homedeptcode])
    
    return entries

def main():
    start_time = time.time()

    # Load data
    df_coa = load_chart_of_accounts()
    df_toi = load_payroll_data()
    
    # Process data
    df_toi['Pay Date'] = pd.to_datetime(df_toi['Pay Date']).dt.date
    print(f'This input file is for Company {df_toi["Company Code"].iloc[0]}')

    money_headers = get_money_headers(df_toi)
    
    # Group and process data
    df_groupby = df_toi.groupby(['Batch Number', 'Home Department Code', 'Location Description', 'Pay Date'])
    
    # Create output dataframe
    df_output = pd.DataFrame(columns=['Pay Date', 'Account Number', 'Description', 'Debit Amount', 'Credit Amount', 'Location', 'Dept'])
    
    # Process each group
    for groupings, row in df_groupby:
        entries = process_payroll_row(groupings, row, df_coa, money_headers)
        for entry in entries:
            df_output.loc[len(df_output.index)] = entry

    # Save results
    running_time = time.time() - start_time
    print("Save the Output File...")
    
    app = tk.Tk()
    app.title("Save File As")
    status_label = tk.Label(app, text="", fg="green")
    status_label.pack()
    save_button = tk.Button(app, text="Save as", command=save_dataframe(df_output, status_label))
    save_button.pack(padx=20, pady=10)
    
    print(f"The execution time is: {running_time}")

if __name__ == "__main__":
    main()