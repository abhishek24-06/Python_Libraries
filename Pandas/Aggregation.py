import pandas as pd

df=pd.read_csv("pokemon.csv")
# for whole Database
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.count())

#for single column
print(df["Height"].mean())
print(df["Weight"].max())
print(df["Height"].min())
print(df["Height"].count())
print(df["Height"].min())

group = df.groupby("Type1")

print(group["Height"].sum())
print(group["Weight"].max())
print(group["Height"].count())

