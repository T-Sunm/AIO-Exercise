from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

"""
numpy.random.choice(a, size=None, replace=True, p=None)
a: Mảng đầu vào hoặc số nguyên. Nếu a là một số nguyên,
thì numpy.random.choice sẽ tạo ra một mảng từ 0 đến a-1, sau đó chọn ngẫu nhiên phần tử từ mảng này.
Nếu a là một mảng, thì hàm sẽ chọn từ các phần tử của mảng đó.
size: Số lượng phần tử cần chọn. Nếu size=None, hàm sẽ trả về một phần tử duy nhất.
 Nếu bạn chỉ định size, hàm sẽ trả về một mảng với số phần tử tương ứng.

replace: Quyết định có cho phép chọn lặp lại hay không.
Nếu replace=True, các phần tử có thể được chọn nhiều lần. Nếu replace=False, mỗi phần tử chỉ có thể được chọn một lần.
"""

class KMeans:
  def __init__(self, k=3, max_iters=100) -> None:
    self.k = k                  # số cụm
    self.max_iters = max_iters  # Số vòng lặp tối đa
    self.centroids = None       # Tọa độ tâm cụm
    self.clusters = None        # Cụm của từng điểm dữ liệu

  def initialize_centroids(self, data):
    """
    Khởi tạo ngẫu nhiên tâm cụm
    Parameters:
        data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
    Return:
        None
    """
    rng = np.random.default_rng(seed=42)  # Tạo generator mới với seed
    self.centroids = data[rng.choice(data.shape[0], self.k, replace=False)]
    return self.centroids

  def euclidean_distance(self, x1, x2):
    """
    Tính khoảng cách euclide giữa 2 điểm dữ liệu
    Parameters:
        x1 (numpy.ndarray): điểm dữ liệu 1
        x2 (numpy.ndarray): điểm dữ liệu 2
    Return
        float: khoảng cách Euclid
    """

    return np.sqrt(np.sum(np.power(x1 - x2, 2), axis=1))

  def assign_clusters(self, data: np.ndarray):
    """
    Phân cụm dữ liệu
    Parameters:
        data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
    Return:
        numpy.ndarray: mảng chứa cluster của từng điểm dữ liệu
    """

    distance = np.array([self.euclidean_distance(
        data, centroid) for centroid in self.centroids]).T

    return np.argmin(distance, axis=1)

  def update_centroids(self, data: np.ndarray):
    '''
    Parameters:
        data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
    Return:
        numpy.ndarray: mảng chứa tâm cụm mới
    '''
    self.clusters = self.assign_clusters(data)
    centroids_new = np.array([data[self.clusters == k].mean(axis=0)
                              for k in range(self.k)])

    return centroids_new

  def fit(self, data: np.ndarray):
    """
       Hàm huấn luyện
       Parameters:
           data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
       Return:
           None
    """
    self.initialize_centroids(data)
    self.clusters = self.assign_clusters(data)
    for _ in range(self.max_iters):
      centroids_new = self.update_centroids(data=data)
      if np.all(centroids_new == self.centroids):
        break

      self.centroids = centroids_new

    print(self.centroids)
    self.plot_clusters(data)

  def plot_clusters(self, data):
    plt.scatter(x=data[:, 0], y=data[:, 1], marker='o', c=self.clusters)
    plt.scatter(x=self.centroids[:, 0], y=self.centroids[:, 1],
                marker='x', c="red", s=300)
    plt.title("Initial Dataset")
    plt.xlabel("Sepal length (cm)")
    plt.ylabel("Sepal width(cm)")
    plt.show()

  def predict(self, data_test):
    return self.assign_clusters(data_test)


def main():
  iris_dataset = load_iris()
  data = iris_dataset.data[:, :2]
  kmeans = KMeans(k=3)
  kmeans.fit(data=data)
  test_data = np.array([[5.0, 3.5], [6.0, 2.7]])
  print(kmeans.predict(test_data))


if __name__ == "__main__":
  main()
