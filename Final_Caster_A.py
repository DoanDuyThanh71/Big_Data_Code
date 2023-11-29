import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('weatherHistory.csv')

# print(df)

X = df['Apparent Temperature (C)']
Y = df['Humidity']
plt.scatter(X,Y, label ="DU LIEU", color='green', marker='D')
plt.title("Bieu Do Scatter")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.legend()
plt.show()