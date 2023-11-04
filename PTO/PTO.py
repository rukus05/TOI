import tkinter as tk
import pandas as pd
import time
from fns import FilePrompt
from fns import save_dataframe
from definitions import pto_gl_dict as gldict
from definitions import locations_dict as ld


def main():

    start = time.time()
    # Select input (Raw data) file.
    f = FilePrompt()
    df_toi = pd.read_excel(f)
    df_toi = df_toi.reset_index()


    df_groupby = df_toi.groupby(['Company', 'Location', 'Department'])

    df_Output = pd.DataFrame(columns=['Company', 'Location', 'Department','PTO Expense', 'GL Account'])

    for groupings, row in df_groupby:
        pto = row['PTO Expense'].sum()
        location_code = ld[groupings[1].strip()]
        gl_no = gldict[groupings[2]]

        df_Output.loc[len(df_Output.index)] = [groupings[0], location_code, groupings[2], pto, gl_no]

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