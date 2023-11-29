import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#đọc dữ liệu
df = pd.read_csv('weatherHistory.csv')

humidity_input = float(input("Nhập độ ẩm muốn dự báo:"))
# Dữ liệu mẫu (độ ẩm và nhiệt độ)
humidity = df[['Humidity']]  # Độ ẩm (%)
temperature = df['Temperature (C)']  # Nhiệt độ (°C)

print(humidity)
print(temperature)
#Trong bài này, chúng ta chưa cần chia tệp dữ liệu

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
humidity = np.array(humidity)  # Reshape để phù hợp với scikit-learn
model.fit(humidity, temperature)


# Dự đoán nhiệt độ dựa trên độ ẩm
new_humidity = np.array([[humidity_input]])  # Độ ẩm mới để dự đoán nhiệt độ
predicted_temperature = model.predict(new_humidity)

print(f"Dự đoán nhiệt độ cho độ ẩm {humidity_input}% là:", predicted_temperature[0], "°C")

