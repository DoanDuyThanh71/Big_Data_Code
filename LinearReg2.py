import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#đọc dữ liệu
df = pd.read_csv('weatherHistory.csv')

wind_speed_input = float(input("Nhập tốc độ gió muốn dự báo:"))
# Dữ liệu mẫu (tốc độ gió và tầm nhìn)
wind_speed = df['Wind Speed (km/h)']  # Tốc độ gió (m/s)
visibility = df['Visibility (km)']  # Tầm nhìn (km)

print(wind_speed)
print(visibility)
#Trong bài này, chúng ta chưa cần chia tệp dữ liệu


# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
wind_speed = np.array(wind_speed).reshape(-1, 1)  # Reshape để phù hợp với scikit-learn
model.fit(wind_speed, visibility)

# Nhập giá trị tốc độ gió mới để dự đoán tầm nhìn
new_wind_speed = np.array([[wind_speed_input]])  # Tốc độ gió mới để dự đoán tầm nhìn
predicted_visibility = model.predict(new_wind_speed)

# In ra dự đoán tầm nhìn tương ứng với tốc độ gió mới
print("Dự đoán tầm nhìn cho tốc độ gió", new_wind_speed[0][0], "m/s là:", predicted_visibility[0])

