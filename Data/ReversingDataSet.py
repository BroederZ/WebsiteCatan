from pathlib import Path
import pandas as pd

#open path to the excel file
excel_path = Path(__file__).resolve().with_name("CatanRawDataModified.xlsx")
#print("excel_path:", excel_path)
#leest de hele file
file_original = pd.read_excel(excel_path, sheet_name="Blad1", engine="openpyxl")
file = file_original.copy() # Create a copy of the original file to avoid modifying it directly
print("file:", file)

#Reverse the order of the data to have the oldest first
data = file.iloc[::-1].reset_index(drop=True)
print("omgekeerde data:", data)