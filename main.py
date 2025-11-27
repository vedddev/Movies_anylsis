import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport


path="F:\\Data sciance\\Project\\Movies\\TMDb_updated (1).csv"
df=pd.read_csv(path)

print(df.head())

subset=df["overview"]
print(subset)

df=df.fillna(df.ffill(),inplace=False)
print(df.isnull().sum())

profile=ProfileReport(df)
profile.to_file(output_file="Movie.html")

