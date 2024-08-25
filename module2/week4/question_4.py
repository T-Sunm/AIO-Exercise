import numpy as np
# Question 4

def compute_correlation_cofficient(X, Y):
  N = len(X)
  numerator = 0
  denominator = 0

  numerator = N * np.einsum('i,i -> ', X, Y)
  numerator -= sum(X) * sum(Y)

  denominator = np.sqrt(N * np.einsum('i,i-> ', X, X) - sum(X)**2)
  denominator *= np.sqrt(N * np.einsum('i,i-> ', Y, Y) - sum(Y)**2)

  return np.round(numerator / denominator, 2)

def main():
  X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
  Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
  print("Correlation : ", compute_correlation_cofficient(X, Y))


if __name__ == "__main__":
  main()
