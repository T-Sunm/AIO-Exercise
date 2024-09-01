import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


def main():
  iris_x, iris_y = datasets.load_iris(return_X_y=True)
  # split train:test = 8:2

  x_train, x_test, y_train, y_test = train_test_split(
      iris_x,
      iris_y,
      test_size=0.2,
      random_state=42
  )

  scaler = StandardScaler()
  # fit Tính toán các thống kê (giá trị trung bình và độ lệch chuẩn) từ dữ liệu X_train, Transform: Sử dụng các thống kê đã tính toán để chuẩn hóa dữ liệu X_train.
  x_train = scaler.fit_transform(x_train)
  # khi fit ở trên thì có mean và std của train , dùng nó chuẩn hóa tiếp cho test
  x_test = scaler.transform(x_test)

  knn_classifier = KNeighborsClassifier(n_neighbors=5)
  knn_classifier.fit(x_train, y_train)

  y_pred = knn_classifier.predict(x_test)
  print(accuracy_score(y_pred, y_test))


