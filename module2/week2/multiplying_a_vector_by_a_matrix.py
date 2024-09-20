import numpy as np

def matrix_multi_vector(matrix: np, vector: np):
  result = matrix.dot(vector)

  return result

def matrix_multi_vector_with_einsum(matrix: np, vector: np):
  result = np.einsum("ij,j->i", matrix, vector)

  return result


def main():
  rng = np.random.default_rng(7)
  A = rng.random((3, 5))
  v = rng.random(5)

  print("Multiplying a vector by a matrix:", matrix_multi_vector(A, v))
  print("Multiplying a vector by a matrix with einsum :",
        matrix_multi_vector_with_einsum(A, v))


if __name__ == "__main__":
  main()
