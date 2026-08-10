import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 3, 8, 15, 24, 35])
y2 = np.array([0, 2, 6, 12, 20, 30])
y3 = np.array([0, 1, 4, 9, 16, 25])
y4 = np.array([0, 4, 12, 24, 40, 60])
y5 = np.array([0, 5, 10, 15, 20, 25])

plt.plot(x,y1, marker = 'o')
plt.plot(x,y2, marker = 'h')
plt.plot(x,y3, marker = 'v')
plt.plot(x,y4, marker = 's')
plt.plot(x,y5, marker = 'd')

plt.title("Totale punten behaald")
plt.xlabel("Datum")
plt.ylabel("Punten")
plt.legend(["Speler 1", "Speler 2", "Speler 3", "Speler 4", "Speler 5"])
# voor iedereen een eigen marker / lijnstijl

plt.show()








