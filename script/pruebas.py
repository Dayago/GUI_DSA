import pandas as pd



"""Read data from csv"""
df = pd.read_csv("..\Documents\materials.csv")
df = df.drop("Unnamed: 0",axis=1)
print(df)

titles = df.columns.values

duplicate = df[df.duplicated(subset =['description'], keep =False)]
df = df.drop_duplicates()
print(duplicate)
print(df)

df = df.to_csv("..\Documents\data_materials.csv", index=False)