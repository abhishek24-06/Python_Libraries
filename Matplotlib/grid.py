import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y=[0,56,34,78,1,90,23,74,66,17]

plt.grid(axis="both",
         color="black",
         linewidth=1,
         linestyle="dashed")

plt.plot(x,y, marker=".",
              markersize="15",
              linewidth="3")
plt.show()