#simple file to convert excel files to csv format with various delimeters

#module import
import pandas as pd
import tkinter as tk
from tkinter import filedialog


#open file with dialog
root = tk.Tk()
root.withdraw()
filetosave_path = filedialog.askopenfilenames(initialdir = "E:\python projects\csv converter",
                                            title = "Select template to convert",
                                            filetypes = [("excel files","*.xlsx"),("excel files,*.xls")])
def file_mod(filetosave_a):
    return filetosave_a[(filetosave_a.kolumna1 != "a") & (filetosave_a.kolumna2 != "b") & (filetosave_a.kolumna3 != "c")]
    

def saving_to_formats(filetosave_p, path):
    filetosave_p.to_csv(path_or_buf=path.split(".")[0] + "_csv.csv")  #save into CSV with "_csv" added to name 
    filetosave_p.to_csv(path_or_buf=path.split(".")[0] + "_pipe.csv", sep= "|")  #save into CSV with "_pipe" added to name and with pipe separator
    filetosave_p.to_csv(path_or_buf=path.split(".")[0] + "_publish.xlsx")  #save into Excel file with name extension "_publish"
# files are so fucking big after this, find sol to make them thiner | _publish.xlsx does not open. maybe xls?

# iteration throught chosen excel files calles
def file_iteration(filetosave_path_p):
    for i in filetosave_path_p:
        filetosave = pd.read_excel(i)
        saving_to_formats(file_mod(filetosave), i)


file_iteration(filetosave_path)



