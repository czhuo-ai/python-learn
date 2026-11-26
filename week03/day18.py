import pandas as pd

df=pd.read_csv("../week02/expenses.csv")
print(df)

print("---")
print(df["金额"].sum())
print(df["金额"].mean())

print(df[df["金额"]>10])