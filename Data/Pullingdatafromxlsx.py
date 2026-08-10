from pathlib import Path
import matplotlib.pyplot as plt
from numpy import save
import pandas as pd
#import openpyxl

#open path to the excel file
excel_path = Path(__file__).resolve().with_name("Catan_ostuni.xlsx")
#print("excel_path:", excel_path)
#leest de hele file
file = pd.read_excel(excel_path, sheet_name="Blad1", engine="openpyxl")
#print("file:", file)

# Get all columns (except index/names)
data = file[["Datum","Max", "Enzo", "Antoine", "Ma", "Pa"]]
#data["Datum"] = pd.to_datetime(data["Datum"], format="%d-%m-%Y") #The right format for the date
data = file.iloc[::-1].reset_index(drop=True) #Reverse the order of the dates to have the oldest first
#print("data:", data)

# Plot all cumulative scores
plt.figure(figsize=(10, 6))
for column in data.select_dtypes(include=['number']).columns:
   plt.plot(data["Datum"], data[column].cumsum(), label=column, marker='o')#Elke lijn een specifiek marker geven
   #print(data[column].cumsum())
plt.xlabel("Datum")#verander naar datum in het figuur zelf
plt.ylabel("Totaal behaalde punten")
plt.title("Catan Scores - Cumulative")
plt.legend()

#save naar de Graphs map in de Data map
save_path = Path(__file__).resolve().parent / "Graphs"
#print("save_path:", save_path) # for checking the path
#save_path.mkdir(exist_ok=True) # To remove the error codes; it makes the map
save_path = save_path / "catan_totalscores.png"
plt.savefig(save_path, dpi=300, bbox_inches="tight")
#plt.show() #FigureCanvassAgg is non-interactive dus word niet getoond.
print("Plot saved as catan_totalscores.png in path:", save_path)