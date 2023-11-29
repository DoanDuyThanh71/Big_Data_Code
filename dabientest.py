import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Đọc dữ liệu
df = pd.read_csv('weatherHistory.csv')
wind_speed_input = float(input("Nhập tốc độ gió: "))
humidity_input = float(input("Nhập độ ẩm: "))
pressure_input = float(input("Nhập áp suất: "))

# Lựa chọn các biến độc lập và phụ thuộc
X = df[['Wind Speed (km/h)', 'Humidity', 'Pressure (millibars)']]  # Biến độc lập
y = df['Visibility (km)']  # Biến phụ thuộc

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X, y)

# Nhập giá trị mới của các biến độc lập để dự đoán tầm nhìn
new_data = np.array([[wind_speed_input, humidity_input, pressure_input]]) 
# Nhập giá trị mới của tốc độ gió, độ ẩm, và áp suất
predicted_visibility = model.predict(new_data)

# In ra dự đoán tầm nhìn tương ứng với giá trị mới của các biến độc lập
print("Dự đoán tầm nhìn cho tốc độ gió {}, độ ẩm {}, và áp suất {} là: {}".format(
    new_data[0][0], new_data[0][1], new_data[0][2], predicted_visibility[0]
))

