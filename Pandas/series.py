import pandas as pd

data = [100,200,300]

series=pd.Series(data)
print(series)

#custom index

data=[100,200,300]

New_series=pd.Series(data,index=["a","b","c"])

print(New_series.iloc[2])
New_series.loc["a"]=150
print(New_series.loc["a"])

#filtering
data=[100,200,300,400,500,600]

series=pd.Series(data,index=["a","b","c","d","e","f"])
print(series[series<500])