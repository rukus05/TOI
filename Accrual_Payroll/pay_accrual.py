import tkinter as tk
import pandas as pd
import time
import calendar
import datetime
import numpy as np
from zpack.fns import FilePrompt
from zpack.fns import save_dataframe
from toi_module.mappings import pay_mappings as pa_dict
from toi_module.definitions import locations_dict as ld


def main():

    

    # Prompt for current accrual date info
    current_year = int(input("Please enter the 4 digit year for this accrual: "))
    current_month = int(input("Please enter the 2-digit month for this accrual: "))
    last_day = int(input("Please enter the 2-digit day for the last pay period in the month: "))
    accrue_from = last_day + 1
    # Set the start for the accrual
    start_accrual = datetime.date(current_year, current_month, accrue_from)
    # Determine the last day of the accrual month
    end_accrual = datetime.date(current_year, current_month, calendar.monthrange(current_year, current_month)[1])
    
    # Begin calculation of runtime
    start = time.time()
    # Determine the day of the week the last day lands on
    dow = end_accrual.strftime("%A")
    #print(dow)
    #print(start_accrual, end_accrual)
    
    # Calculate the number of business days between start and end of accrual
    if dow == 'Saturday' or dow == 'Sunday':
        business_days = np.busday_count(start_accrual, end_accrual)
    else:
        business_days = np.busday_count(start_accrual, end_accrual) + 1
    # Print the number of Business days.
    print('The number of business days for this accrual is: ', business_days)
    accrual_hours = business_days * 8
    # Select input (Raw data) file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)
    df_toi = df_toi.reset_index()

    df_toi['Accrued Payroll'] = df_toi['Hourly Rate'].mul(accrual_hours)
    df_toi['Accrued Payroll Tax'] = df_toi['Accrued Payroll'].mul(0.0765)

    df_groupby = df_toi.groupby(['Company Code', 'Location Description', 'Department'])


    df_Output = pd.DataFrame(columns=['Company Code', 'Location Description', 'Department','Accrued Payroll', 'Description', 'GL Account'])

    for groupings, row in df_groupby:
        acc_pay = row['Accrued Payroll'].sum()
        acc_pt = row['Accrued Payroll Tax'].sum()
        location_code = ld[groupings[1].strip()]
        pay_gl_no = pa_dict[groupings[2]][0]
        ac_p_gl_no = pa_dict[groupings[2]][1]
        if acc_pay != 0:
            df_Output.loc[len(df_Output.index)] = [groupings[0], location_code, groupings[2], acc_pay, 'Accrued Payroll', pay_gl_no]
            df_Output.loc[len(df_Output.index)] = [groupings[0], location_code, groupings[2], acc_pt, 'Accrued Payroll Tax', ac_p_gl_no]

    # Start the "Save As" dialog box.
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