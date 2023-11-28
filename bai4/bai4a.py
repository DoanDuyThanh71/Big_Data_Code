import pandas as pd 
import numpy as np

df = pd.read_csv('mtcars.csv')
df_numerics = df.select_dtypes(include=['number'])

print(df_numerics)



