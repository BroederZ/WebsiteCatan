from pathlib import Path
import openpyxl
import pandas as pd

#open path to the excel file
name_excelfile = "Catan_Ostuni.xlsx"
excel_path = Path(__file__).resolve().with_name(name_excelfile)
#print("excel_path:\n", excel_path)

#Getting sheet names
wb = openpyxl.load_workbook(excel_path)
sheet_names = wb.sheetnames
#print("sheet_names:\n", sheet_names)

#leest de hele file
file_original = pd.read_excel(excel_path, sheet_name="Blad1", engine="openpyxl")

#Create a copy of the original file
file = file_original.copy() 
#print("file:\n", file)

#Right format for the date
data = file[["Datum"]]
print(file["Datum"].unique())
data["Datum"] = pd.to_datetime(data["Datum"], format="%d-%m-%Y")


#Reverse the order of the data to have the oldest first
d1 = data["Datum"][0]
d2 = data["Datum"][1]
if d1 > d2:
   print("No need to reverse the order")
   data = file
else:
   data = file.iloc[::-1].reset_index(drop=True)
   print("omgekeerde data:\n", data)


df = pd.DataFrame(data)

#maak file met naam juiste naam
name_excelfile_saved = "Catan_Ostuni_Goed.xlsx"
save_excel_path = Path(__file__).resolve().with_name(name_excelfile_saved)
df.to_excel(save_excel_path,sheet_name="Alles", index=False)
print("Reversed data saved as", name_excelfile_saved, "in path:", save_excel_path)

