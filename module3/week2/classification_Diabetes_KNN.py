import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
def main():
  diabetes_x, diabetes_y = datasets.load_diabetes(return_X_y=True)

# split train:test = 8:2
  x_train, x_test, y_train, y_test = train_test_split(
      diabetes_x,
      diabetes_y,
      test_size=0.2,
      random_state=42
  )

  scaler = StandardScaler()
  # fit Tính toán các thống kê (giá trị trung bình và độ lệch chuẩn) từ dữ liệu X_train, Transform: Sử dụng các thống kê đã tính toán để chuẩn hóa dữ liệu X_train.
  x_train = scaler.fit_transform(x_train)
  # khi fit ở trên thì có mean và std của train , dùng nó chuẩn hóa tiếp cho test
  x_test = scaler.transform(x_test)

  knn_regressor = KNeighborsRegressor(n_neighbors=5)
  knn_regressor.fit(x_train, y_train)

  y_pred = knn_regressor.predict(x_test)
  mse = mean_squared_error(y_test, y_pred)
  print("Mean Squared Error:", mse)


if __name__ == "__main__":
  main()
