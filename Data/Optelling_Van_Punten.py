from pathlib import Path
import matplotlib.pyplot as plt
from numpy import save
import pandas as pd
import openpyxl

name_excelfile = "Catan_VerwerkteData_Alles.xlsx"
#name_excelfile = "Catan_Ostuni.xlsx" #aanpassen door file
name_graphfile = "Catan_TotaleScore_Ostuni.png" #aanpassen door file

#open path to the excel file
excel_path = Path(__file__).resolve().with_name(name_excelfile)
#print("excel_path:\n", excel_path)

#Getting sheet names
wb = openpyxl.load_workbook(excel_path)
sheet_names = wb.sheetnames
#print(f"sheet_names:\n {sheet_names})

#leest de hele file
file_original = pd.read_excel(excel_path, sheet_name="Alles", engine="openpyxl")

#Create a copy of the original file
file = file_original.copy() 
#print("file:\n", file)

# Get all columns (except index/names)
data = file[["Datum", "Max", "Enzo", "Antoine", "Ma", "Pa"]]
data["Datum"] = pd.to_datetime(data["Datum"], format="%d-%m-%Y") #The right format for the date
print(f"Datums:/n{data["Datum"]}")

#Reverse the order of the data to have the oldest first
d1 = data["Datum"][0]
d2 = data["Datum"][1]
if d1 < d2:
   print("No need to reverse the order")
   data = file
else:
   data = file.iloc[::-1].reset_index(drop=True)
   print(f"omgekeerde data:\n{data}")


# Plot all cumulative scores
plt.figure (figsize=(10, 6))
for column in data.select_dtypes(include=['number']).columns:
   plt.plot(data["Datum"], data[column].cumsum(), label=column, marker='o')#Elke lijn een specifiek marker geven
numeric_columns = data.select_dtypes(include=['number']).columns
print(f"Columns:, {len(numeric_columns)}")
plt.xlabel("Datum")#De agen waarop niet gespeeld weghalen.
plt.ylabel("Totaal behaalde punten")
plt.title("Catan Scores - Cumulative")#Andere titel
plt.legend()

#save naar de Graphs map in de Data map
save_path = Path(__file__).resolve().parent / "Graphs"
#print("save_path:", save_path) # for checking the path
#save_path.mkdir(exist_ok=True) # To remove the error codes; it makes the map
save_path = save_path / name_graphfile
plt.savefig(save_path, dpi=300, bbox_inches="tight")
#plt.show() #FigureCanvassAgg is non-interactive dus word niet getoond.
print(f"Plot saved as {name_graphfile} in path: {save_path}")