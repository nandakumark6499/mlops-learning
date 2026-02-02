import pandas as pd

df = pd.read_csv("titanic.csv")

df = df.drop(columns=["deck"])

df["age"] =  df["age"].fillna(df["age"].median())

df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df["embark_town"] = df["embark_town"].fillna(df["embark_town"].mode()[0])

df.to_csv("clean_data.csv", index = False)

print("Cleaned data saved as clean_data.csv")
print(df.info())
