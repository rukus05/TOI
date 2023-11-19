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


    df_toi['Invoice Date'] = pd.to_datetime(df_toi['Invoice Date'])
    df_toi['Month'] = df_toi['Invoice Date'].dt.strftime('%b %Y')
    #df_toi['Month'] = df_toi['Invoice Date'].dt.to_period('M')

    #unique_months = sorted(df_toi['Invoice Date'].dt.to_period('M').unique())
    #unique_months = sorted(df_toi['Invoice Date'].dt.to_period('M').unique())
    # Extract out only the year and month of the date.
    #month_year_list = [dt.strftime("%Y-%m") for dt in unique_months]
    #print(month_year_list)
    #um_dict = []
    # Create a dictionary to hold the Monthly sums.
    #monthly_sums ={}
    # Create a dictionary based on unique monts
    #for um in month_year_list:
    #    um_dict.append(um)
    #    monthly_sums[str(um)] = 0
    #print(monthly_sums)
    #others = ['GL Code', 'GL Name', 'Vendor', 'Location', 'Department', 'Description', 'Accrual Amount']
    # Aggregate into a Headers list
    #new_list = others + unique_months
    
    # Create an output dataframe based on the new list above
    #df_Output = pd.DataFrame(columns = new_list)

    # df_groupby = df_toi.groupby(['GL Code', 'Vendor', 'Location', 'Department']).agg({'Month' : ['count'], 'Amount' : 'sum'}).reset_index()
    # Account Code is GL Name; Supplier Name is Vendor;  Custom 5 - Code is Location;  Custom 3 - Code is Department
    df_groupby = df_toi.groupby(['Account Code', 'Supplier Name', 'Custom 5 - Code', 'Custom 3 - Code', 'Month'])

    result_df = df_groupby.agg({'Amount' : 'sum'})

    result_df = result_df.reset_index()
    result_df['Custom 5 - Code'] = result_df['Custom 5 - Code'].astype(str)
    result_df['Custom 3 - Code'] = result_df['Custom 3 - Code'].astype(str)
    #print(result_df.columns)
    #amt = result_df['Account Code']
    #print(amt)
    #combined_columns = result_df[['Account Code', 'Supplier Name']]
    #print(combined_columns)
    #result_df['Combined'] = str(result_df['Account Code'] + result_df['Supplier Name'] + str(result_df['Custom 5 - Code']) + str(result_df['Custom 3 - Code']))
    #unique_combined_list = list(result_df['Combined'].unique())
    #print(unique_combined_list[100])
    uniqueAC = result_df['Account Code'].unique()
    uniqueSN = result_df['Supplier Name'].unique()
    uniqueC5 = result_df['Custom 5 - Code'].unique()
    uniqueC3 = result_df['Custom 3 - Code'].unique()
    
    for ac in uniqueAC:
        for sn in uniqueSN:
            for c5 in uniqueC5:
                for c3 in uniqueC3:
                    for index, row in result_df.iterrows():
                        if (row['Account Code'] == ac) and (row['Supplier Name'] == sn) and (row['Custom 5 - Code'] == c5) and (row['Custom 3 - Code'] == c3):
                            print(row['Amount'])
                        
                

    # Start the "Save As" dialog box.
    app = tk.Tk()
    app.title("Save File As")
    status_label = tk.Label(app, text="", fg="green")
    status_label.pack()
    save_button = tk.Button(app, text="Save as", command=save_dataframe(result_df, status_label))
    save_button.pack(padx=20, pady=10)
   
    runningtime = time.time() - start
    print("The execution time is:", runningtime)




if __name__ == "__main__":
    main()