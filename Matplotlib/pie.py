import matplotlib.pyplot as plt
import numpy as np

libraries=["Numpy","Pandas","Polars","Matplotlib","Scikit learn"]
importance=np.array([250,350,200,200,400])
colors=["red","green","blue","yellow","orange"]

plt.pie(importance, labels=libraries,
                    autopct="%1.1f%%",
                    colors=colors,
                    explode=[0.1,0.1,0.1,0.1,0],
                    shadow="True",
                    startangle=180)

plt.title("Importance given")
plt.show()
