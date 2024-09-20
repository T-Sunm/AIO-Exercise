import numpy as np
def compute_median(x):
  size = len(x)
  x = np.sort(x)
  if size % 2 != 0:
    return x[((size + 1) // 2) - 1]
  else:
    # vì phần tử của list bắt đầu từ 0 nên phải - 1
    med_1 = x[(size // 2) - 1]
    med_2 = x[(size // 2) + 1 - 1]
    print(med_1, med_2)
    return (med_1 + med_2) / 2

def main():
  X = [1, 5, 4, 4, 9, 13]
  print("Mean : ", compute_median(X))


if __name__ == "__main__":
  main()
