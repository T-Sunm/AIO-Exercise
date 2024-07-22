import numpy as np

def matrix_multi_matrix(matrix1: np, matrix2: np):
  result = matrix1.dot(matrix2)

  return result

def matrix_multi_matrix_with_einsum(matrix: np, matrix2: np):
  result = np.einsum("ij,jk->ik", matrix, matrix2)

  return result


def main():
  rng = np.random.default_rng(7)
  A = rng.random((3, 5))
  B = rng.random((5, 4))

  print("Multiplying a vector by a matrix:", matrix_multi_matrix(A, B))
  print("Multiplying a vector by a matrix with einsum :",
        matrix_multi_matrix_with_einsum(A, B))


if __name__ == "__main__":
  main()
