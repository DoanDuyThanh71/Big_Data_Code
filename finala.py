import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weatherHistory.csv')

humidity_input = float(input("Nhap do am muon du bao ra nhiet do: "))

X = df[['Humidity']]
Y = df['Temperature (C)']

model = LinearRegression()
X = np.array(X)
model.fit(X,Y)

new_Humidity_input = np.array([[humidity_input]])
predicted_temperature = model.predict(new_Humidity_input)
print(predicted_temperature)


