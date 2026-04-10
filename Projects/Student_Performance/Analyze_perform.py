import pandas as pd

df=pd.read_csv("Student_data.csv") #Export csv
# print(df.to_string()) #dispay most dataset

rows,kidney = df.shape #print total rows and col
# print("Rows: ",rows)
# print("Columns: ",kidney)

# print(df.head(5)) #print first n rows
# print(df.tail(7)) #print last n rows

# print(df.columns) #print col 

# print(df.info()) #print info of entire dataset

# df["math score"]=df["math score"].astype(int)
# print(df.describe())

# print(df.isnull())

# print(df["gender"].value_counts()) #to print total appearance

# print(df.groupby("division")["gender"].count())

df=pd.read_csv("Student_data.csv")


print("Total no of students in the dataset :", df.shape[0])
print("Name of the columns: ", df.columns)

print("Total males and females:", df["gender"].value_counts())

print("Total students in each divison: ", df.groupby("division")["gender"].value_counts())

print("Total students by Education: ",df.groupby("parental level of education")["gender"].value_counts())

print("Average score of math: ",df["math score"].mean())
print("Average score of reading: ",df["reading score"].mean())
print("Average score of writing: ",df["writing score"].mean())

####################################
df["Total"]=df["math score"]+df["reading score"]+df["writing score"]

toppers=df.sort_values("Total",ascending=False).head(5)

print(toppers[["Total","math score","writing score","reading score"]])
####################################
df["Lowest score"]=df["math score"]+df["reading score"]+df["writing score"]

low5=df.sort_values(["Lowest score"]).head(5)

print(low5[["Lowest score","math score","writing score","reading score"]])
####################################

#Overall Average in Percentage#
df["Total"]=df["math score"]+df["reading score"]+df["writing score"]
avg_score=df["Total"].mean()
Overall_Percentage=(avg_score/300) * 100
print("The Overall Average Percentage is ",Overall_Percentage,"%")
####################################

#Gender-based Performance Analysis
print("The average score of math of student is : ",df.groupby("gender")["math score"].mean())
print("The average score of reading of student is : ",df.groupby("gender")["reading score"].mean())

#Print only one category avg instead of all categories 
print("The average of writing score for male is :",df[df["gender"]=="male"]["writing score"].mean())

#Even better Approach
female_writing_score= df.groupby("gender")["writing score"].mean()
print("The average of  writing score for female is :",female_writing_score["female"])

#which gender perfomrance best 
overall=df.groupby("gender")[["math score","writing score","reading score"]].mean().mean(axis=1)

best_gender=overall.idxmax()
best_score=overall[best_gender]
print(f"The gender which performs the best overall is: {best_gender} with a score of {best_score} ")

#How many students have standard lunch and free/reduced lunch?
counts=df["lunch"].value_counts()
print("Total students with standard lunch: ",counts["standard"])
print("Total students with free/reduced lunch: ",counts["free/reduced"])
print("THe average of standard lunch is: ",counts["standard"])

# Lunch=df.groupby("lunch")[""]

Lunch=df.pivot_table(index="lunch",values=["math score","writing score","reading score"],aggfunc="mean")
print(Lunch)

df["math score"].hist()
df.groupby("gender")["math score"].mean().plot(kind="bar")