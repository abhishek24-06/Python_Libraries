import pandas as pd

df=pd.read_csv("pokemon.csv")

#drop columns
# df=df.drop(columns=["Legendary","No"])
# print(df)

# #handle missing data
# df=df.dropna(subset=["Type2"])
# print(df)

# df=df.fillna({"Type2": "None"})
# print(df)

#fix incosistent value
df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})
print(df.to_string)

#Standardize text
df["Name"]=df["Name"].str.lower()
print(df.to_string)

#Fix data Types
df["Legendary"]=df["Legendary"].astype(bool)
print(df.to_string)

#Remove duplicates
df = df.drop_duplicates()
print(df)
