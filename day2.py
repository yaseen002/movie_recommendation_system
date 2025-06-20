# Import pandas
import pandas as pd

movies = pd.read_csv('movies.csv')
credits = pd.read_csv('credits.csv')

print(movies.shape())
print(movies.head(4))

print(movies.columns.tolist())
print("*"*50)
print(credits.columns.tolist())