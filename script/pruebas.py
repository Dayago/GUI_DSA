import pandas as pd



# df = pd.read_csv("C:\Users\LASER\Documents\Python\datos\Documents\materials.csv")
df = pd.read_csv("..\Documents\materials.csv")

print(df)

titles = df.columns.values

for title in titles:
    print(title)
    print(df[title].nunique())

value_duplicated = df["description"].duplicated()

for enumerate(idx,value) in value_duplicated:
    print(value)