import matplotlib.pyplot as plt
import numpy as np

x=np.array([2020,2022,2024,2026])
y=np.array([90,50,70,80])

plt.title("Happiness Index", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="gold")

plt.xlabel("Year", fontsize=15,
                   family="Arial",
                   fontweight="bold",
                   color="silver")

plt.tick_params(axis="both",
                color="yellow")
plt.ylabel("Values")
plt.plot(x,y)
plt.show()