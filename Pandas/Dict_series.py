import pandas as pd

calories = {"Day1":1800, "Day2": 2100, "Day3": 1900}

series=pd.Series(calories)

print(series[series>2000])

series.loc["Day1"] += 500
print(series)

#excerzise
data=["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard"]

series=pd.Series(data)

print(series)