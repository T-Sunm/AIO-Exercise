import math
import numpy as np
import pandas as pd


def create_train_data():
  #   sài names để gán cột
  data = pd.read_csv('iris.data.txt', header=None, names=[
                     'Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'])
  return data

def compute_prior_probablity(train_data: pd.DataFrame):
  y_train = train_data.iloc[:, -1].values
  y_unique = list(set(y_train))
  prior_count = np.zeros(len(y_unique))
  prior_probablity = {}
  for data in y_train:
    index = y_unique.index(data)
    prior_count[index] += 1

  for label, count in zip(y_unique, prior_count):
    prior_probablity[label] = count / y_train.shape[0]

  return prior_probablity


def gausian_func(x, mean, var):
  return (1 / math.sqrt(var) * math.sqrt(2 * math.pi)) * np.exp(-((x - mean)**2) / (2 * var))

def train_gaussian_naive_bayes(train_data: pd.DataFrame):
  y_train = train_data.iloc[:, -1].values
  y_unique = list(set(y_train))

  conditional_probability = {}

  for y in y_unique:
    # lọc dữ liệu theo từng y = Species để tính điều kiện
    y_data = train_data[train_data.iloc[:, -1] == y]
    y_prob = []
    for col in y_data.columns[: -1]:
      mean_feature = y_data[col].mean()
      var_feature = y_data[col].var()
      y_prob.append((mean_feature, var_feature))

    conditional_probability[y] = y_prob
  return conditional_probability

def prediction_iris(x, prior_probability, conditional_probability):
  probability_species = []
  for species in conditional_probability:
    probability = 1
    for index, (mean, variance) in enumerate(conditional_probability[species]):
      probability *= gausian_func(x[index], mean, variance)
    probability *= prior_probability[species]
    probability_species.append(probability)

  return np.argmax(np.array(probability_species))

def main():
  train_data = create_train_data()

# tìm tiên nghiệm
  prior_probability = compute_prior_probablity(train_data)

# tìm mean và var theo từng condition
  conditional_probability = train_gaussian_naive_bayes(
      train_data)

  print("mean and variance for each species:", conditional_probability)

# Example 1
# X =[ sepal length , sepal width , petal length , petal width ]
  X = [6.3, 3.3, 6.0, 2.5]
  y_train = train_data.iloc[:, -1].values
  y_unique = list(set(y_train))

  pred = y_unique[prediction_iris(
      X, prior_probability, conditional_probability)]
  assert pred == "Iris-virginica"

# Example 2 #########################
 # X =[ sepal length , sepal width , petal length , petal width ]
  X = [5.0, 2.0, 3.5, 1.0]
  pred = y_unique[prediction_iris(
      X, prior_probability, conditional_probability)]
  assert pred == "Iris-versicolor"


# Example 3 #########################
  X = [4.9, 3.1, 1.5, 0.1]
  pred = y_unique[prediction_iris(
      X, prior_probability, conditional_probability)]
  assert pred == "Iris-setosa"

  print("You pass 3 test case")


if __name__ == "__main__":
  main()
