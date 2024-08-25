import numpy as np

def compute_mean(x):
  X = np.array(x)
  return X.mean()


def compute_std(x: list):
  mean = compute_mean(x)
  variance = 0
  for data in x:
    variance += (data - mean)**2

  variance = variance / len(x)

  return np.sqrt(variance)

def main():
  X = X = [171, 176, 155, 167, 169, 182]
  print("Variance : ", compute_std(X))


if __name__ == "__main__":
  main()
