import pandas as pd

df = pd.read_csv('game_results.csv')
print(df.head())
print(df.columns.tolist())