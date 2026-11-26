import json
import pandas as pd

with open("jobs.json",encoding="utf-8") as f:
    raw=json.load(f)

rows=raw["jobs"] if isinstance(raw, dict)else raw

df=pd.DataFrame(rows)
print(df.shape)

print(df["keyword"].value_counts())
print("---")
print(df[df["reject"]==""].value_counts())