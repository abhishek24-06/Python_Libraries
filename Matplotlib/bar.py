import matplotlib.pyplot as plt
import numpy as np

x=(["Milk","Choclate","Mango","Maggi","Mutton"])
y=np.array([2,10,4,2,5])

plt.title("Grocery bought")
plt.xlabel("Groceries")
plt.ylabel("Quantity")

# plt.bar(x,y)
plt.barh(x,y,color="skyblue")
plt.show()