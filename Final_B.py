import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weatherHistory.csv')

Wind_Speed_Input = float(input("nhap toc do gio: "))
Humidity_Input = float(input("Nhap do am: "))

X = np.array(df[['Wind Speed (km/h)', 'Humidity']]) 
Y = np.array(df['Visibility (km)'])

model = LinearRegression()
model.fit(X, Y)

input = np.array([[Wind_Speed_Input, Humidity_Input]])
preditecd = model.predict(input)

print(f"Voi Do Am la {Wind_Speed_Input} va toc do gio la {Humidity_Input} thi tam nhin la {preditecd}",)

