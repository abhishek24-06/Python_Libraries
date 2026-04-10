import matplotlib.pyplot as plt
import numpy as np

year=np.array([2020,2021,2022,2023,2024,2025,2026])

gold=np.array([50000,48000,55000,65000,77000,136000,153000])
silver=np.array([63000,62000,56000,78000,100000,100000,240000])

plt.scatter(year,gold , color="gold",
                        alpha=1,
                        s=100,
                        label="Gold Cost per 10gm")

plt.scatter(year,silver , color="gray",
                          alpha=0.9,
                          s=50,
                          label="Silver cost per 1Kg")

plt.title("Cost Annualy" , fontsize=15)
plt.xlabel("Year")
plt.ylabel("Cost")
plt.legend()

plt.show()