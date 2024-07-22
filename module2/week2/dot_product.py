import numpy as np

def compute_dot_product(vector1: np, vector2: np):
  result = vector1.dot(vector2)

  return result

def compute_dot_product_with_einsum(vector1: np, vector2: np):
  result = np.einsum("i,i->", vector1, vector2)

  return result


def main():
  rng = np.random.default_rng(7)
  vector1 = rng.random(5)
  vector2 = rng.random(5)

  print("Dot product between vector1 and vector2:",
        compute_dot_product(vector1, vector2))
  print("Dot product between vector1 and vector2 with einsum:",
        compute_dot_product_with_einsum(vector1, vector2))


if __name__ == "__main__":
  main()
