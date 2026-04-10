import pandas as pd

df=pd.read_csv("pokemon.csv")
tall_pokemon= df[df["Height"] >= 2]
heavy_pokemon=df[df["Weight"] >= 50]
water_pokemon=df[(df["Type1"]== "Water") |
                 (df["Type2"]== "Poison")]
ff_pokemon=df[(df["Type1"]== "Fire") &
              (df["Type2"]== "Flying")]
# print(tall_pokemon)
# print(heavy_pokemon)
print(water_pokemon)
print(ff_pokemon)