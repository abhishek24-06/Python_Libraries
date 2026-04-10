import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

df = pd.read_csv("pokemon.csv")

types=pd.concat([df["Type1"],df["Type2"]]).dropna()
types=types.value_counts()

plt.figure(figsize=(10,6))
plt.bar(types.index, types.values)
plt.xticks(rotation=45)
plt.title("Pokemon Type Distribution")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# types=pd.concat([df["Type1"],df["Type2"]]).dropna()
# types=types.value_counts()
# print(types)

# colors=plt.cm.tab20.colors

# plt.pie(types, labels=types.index,
#         autopct="%1.1f%%",
#         colors=colors,
#         textprops={"fontsize": 8},
#         )
# # plt.axis("equal")

plt.show()