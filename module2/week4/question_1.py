import numpy as np
def compute_mean(x):
  X = np.array(x)
  return X.mean()


def main():
  X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
  print("Mean : ", compute_mean(X))


if __name__ == "__main__":
  main()
