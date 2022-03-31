import pandas as pd

df = pd.read_csv("final.csv")

df = df[df["Distance"].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

df.to_csv("cleaned_data.csv",index=False)