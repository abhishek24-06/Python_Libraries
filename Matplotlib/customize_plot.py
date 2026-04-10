import matplotlib.pyplot as plt
import numpy as np

x=np.array([2015,2016,2017,2018,2019])
y1=np.array([80,100,105,110,200])
y2=np.array([100,90,95,70,50])
y3=np.array([40,30,10,50,70])

plt.plot(x,y1, marker=".",
               markersize="30",
               markerfacecolor="#d40000",
               markeredgecolor="darkblue",
               linewidth="2"
               )

line_style=dict(marker="*",
                markersize=30,
                markerfacecolor="#01655C",
                markeredgecolor="darkgreen",
                linewidth=2)

plt.plot(x,y2,color="darkgreen", **line_style)
plt.plot(x,y3,color="lightgreen", **line_style)
plt.show()
