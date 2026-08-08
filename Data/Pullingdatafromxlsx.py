from pathlib import Path
import matplotlib.pyplot as plt
from numpy import save
import pandas as pd
#import openpyxl

excel_path = Path(__file__).resolve().with_name("Catan_ostuni.xlsx")
file = pd.read_excel(excel_path, sheet_name="Blad1", engine="openpyxl")
print("excel_path:", excel_path)
print("file:", file)

#x = file["Max"].tolist() #Need to make it a index(.values) or list(.tolist()) from it
#y = file["Enzo"].tolist()
#print(x,y)
#plt.plot(x, y, marker = 'o')
#print(plt.plot(x, y, marker = 'o'))
#plt.show()

# Get all columns (except index/names)
data = file[["Max", "Enzo", "Antoine", "Ma", "Pa"]]
print("data:", data)

# Plot all
for column in data.columns:
   plt.plot(data[column].cumsum(), label=column)
   print(data[column].cumsum())

# Calculate cumulative sum (running total)
#y1_cumsum = 1.cumsum()
#y2_cumsum = 2.cumsum()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(data.columns, label="Max", marker='o')
plt.plot(data.columns, label="Enzo", marker='h')
plt.xlabel("Game Number")#verander naar datum
plt.ylabel("Cumulative Score")
plt.title("Catan Scores - Cumulative")
plt.legend()
#plt.grid(True)

#save naar de Graphs map in de Data map
save_path = Path(__file__).resolve().parent / "Graphs"
#print("save_path:", save_path) # for checking the path
#save_path.mkdir(exist_ok=True) # To remove the error codes; it makes the map
save_path = save_path / "catan_totalscores.png"
plt.savefig(save_path, dpi=300, bbox_inches="tight")
print("Plot saved as catan_totalscores.png in path:", save_path)