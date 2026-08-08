from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
#import openpyxl

excel_path = Path(__file__).resolve().with_name("Catan_ostuni.xlsx")
file = pd.read_excel(excel_path, sheet_name="Blad1", engine="openpyxl")

#x = file["Max"].tolist() #Need to make it a index(.values) or list(.tolist()) from it
#y = file["Enzo"].tolist()
#print(x,y)
#plt.plot(x, y, marker = 'o')
#print(plt.plot(x, y, marker = 'o'))
#plt.show()
# Get all columns (except index/names)
data = file[["Max", "Enzo", "Antoine", "Ma", "Pa"]]

# Plot all
for column in data.columns:
    plt.plot(data[column].cumsum(), label=column)



# Calculate cumulative sum (running total)
y1_cumsum = 1.cumsum()
y2_cumsum = 2.cumsum()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(y1_cumsum, label="Max", marker='o')
plt.plot(y2_cumsum, label="Enzo", marker='h')
plt.xlabel("Game Number")#verander naar datum
plt.ylabel("Cumulative Score")
plt.title("Catan Scores - Cumulative")
plt.legend()
#plt.grid(True)
plt.savefig("catan_scores.png", dpi=300, bbox_inches="tight")
#save naar de data map
print("Plot saved as catan_scores.png")