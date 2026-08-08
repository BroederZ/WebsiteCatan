import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel("Data/Catan_ostuni.xlsx")
x = file["Datum"]
y = file["Punten"]

plt.plot(x, y, marker = 'o')


plt.show()