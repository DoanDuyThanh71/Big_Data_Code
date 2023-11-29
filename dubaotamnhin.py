import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weatherHistory.csv')

wind_speed_input = float(input("Nhap toc do gio muon du bao: "))

wind_speed = df[['Wind Speed (km/h)']]
visibility = df['Visibility (km)']

model = LinearRegression()

model.fit( wind_speed, visibility)

new_wind_speed = np.array([[wind_speed_input]])
preditcted = model.predict(new_wind_speed)

print("Du bao tam nhin cho toc do gio", new_wind_speed[0][0], "m/s", preditcted[0])