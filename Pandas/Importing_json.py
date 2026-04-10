import pandas as pd

df=pd.read_json("pokemon.json")\

print(df.to_string())