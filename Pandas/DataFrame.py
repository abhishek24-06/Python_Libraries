import pandas as pd

data={"Name":["Spongebob","Doreamon","Shinchan"],
      "Age": [20,21,15]
}

df = pd.DataFrame(data,index=["A","B","C"])
print(df)
      
print(df.loc["A"])
print(df.iloc[0])

#Add a new column

df["Job"] = ["Cook","Pilot","Actor"]

print(df)

#Add a new row

new_row=pd.DataFrame([{"Name": "Sandy","Age": 28,"Job": "Engineer"},
                      {"Name": "Vision","Age":29,"Job":"Architect"},
                      ],
                      index=["D","E"])
df=pd.concat([df,new_row])
print(df)