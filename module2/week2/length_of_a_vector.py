import numpy as np

def compute_vector_length(vector):
  len_of_vector = np.linalg.norm(vector)

  return len_of_vector


def main():
  rng = np.random.default_rng(7)
  v = rng.random(5)

  print("Length of a vector v:", compute_vector_length(v))


if __name__ == "__main__":
  main()
