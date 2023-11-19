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


        
    df_toi['GL posting date'] = pd.to_datetime(df_toi['GL posting date'])
    df_toi['Month'] = df_toi['GL posting date'].dt.strftime('%b %Y')
    #df_toi['Month'] = df_toi['Invoice Date'].dt.to_period('M')



    unique_months = sorted(df_toi['Month'].unique(), key=lambda x: pd.to_datetime(x, format='%b %Y'))

    print(unique_months)
    

    # Create a dictionary to hold the Monthly sums.
    monthly_sums ={}
    # Create a dictionary based on unique monts
    for um in unique_months:
    #    um_dict.append(um)
        monthly_sums[str(um)] = 0
    #print(monthly_sums)
    #others = ['GL Code', 'GL Name', 'Vendor', 'Location', 'Department', 'Description', 'Accrual Amount']
    # Aggregate into a Headers list
    #new_list = others + unique_months

    # Create an output dataframe based on the new list above
    # Account Code is GL Name; Supplier Name is Vendor;  Custom 5 - Code is Location;  Custom 3 - Code is Department
    others = ['GL Name', 'Vendor', 'Location', 'Department']
    new_list = others + unique_months + ['Total Sum']
    print(new_list)
    df_Output = pd.DataFrame(columns = new_list)

    # df_groupby = df_toi.groupby(['GL Code', 'Vendor', 'Location', 'Department']).agg({'Month' : ['count'], 'Amount' : 'sum'}).reset_index()
    # Account is GL Name; Vendor ID is Vendor;  Location ID is Location;  Department ID is Department
    df_groupby = df_toi.groupby(['Account', 'Vendor ID', 'Location ID', 'Department ID', 'Month'])
    result_df = df_groupby.agg({'Base amount' : 'sum'}).reset_index()
    result_df['Location ID'].astype(str)
    result_df['Department ID'].astype(str)
    #result_df.to_excel('final_output2.xlsx')
    no_of_rows = len(result_df)
    print(no_of_rows)
    #for row in result_df.itertuples():
    #    ac = row[1]
    #    sn = row[2]
    #    c5 = row[3]
    #    c3 = row[4]
    #    print(row[3])
    #    print(getattr(row, 'Month'), getattr(row, 'Amount'))
        #print(result_df['Amount'][index])
    columns_to_check = [1, 2, 3, 4]
    i=0
    
    for row in result_df.itertuples():
        first_row = result_df.loc[i]
        second_row = result_df.loc[i+1]
        
        if (first_row[0] != second_row[0]) or (first_row[1] != second_row[1]) or (first_row[2] != second_row[2]) or (first_row[3] != second_row[3]):
            #print('New Group')
            monthly_sums[first_row[4]] += first_row[5]
                
            part2 = []
            for value in monthly_sums.values():
                part2.append(value)
            
            part1 = [first_row[0], first_row[1], first_row[2], first_row[3]]
            output_row_data = part1 + part2 + [sum(part2)]
            #print(output_row_data)
            df_Output.loc[len(df_Output.index)] = output_row_data
            
            monthly_sums = {key: 0 for key in monthly_sums}
            
            
        else:
            #print(first_row[0], first_row[1], first_row[2], first_row[3])
            #print('First row and second row are part of the same group!!!!')
            monthly_sums[first_row[4]] += first_row[5]
            #print(monthly_sums)
        
        
            
        #print(result_df.loc[i].compare(result_df.loc[i+1]))
        #print(type(result_df.loc[i].compare(result_df.loc[i+1])))
        #if first_row[4] == 'Oct 2023':
            #print('YES')
        #print(first_row[4], second_row[4])
        i +=1
        if i == no_of_rows -1:
            break
    
                            
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