import pandas as pd

df = pd.read_csv("pokemon.csv")

#Selection by column
# print(df["Name"])
# print(df["Height"])

#multiple col
# print(df[["Name","Height","Weight"]])

#selection by row
df = pd.read_csv("pokemon.csv",index_col="Name")
# print(df.loc["Pikachu"])
# print(df.loc["Charizard",["Height","Weight"]]) #to print only specfic column of index

# print(df.loc["Charizard":"Pikachu",["Height","Weight"]]) #print index to index

print(df.iloc[0:11:1, 0:4])

#search
pokemon=input("Enter Name of Pokemon: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} doesnt exist")