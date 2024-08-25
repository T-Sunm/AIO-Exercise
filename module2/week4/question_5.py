import pandas as pd
import gdown
import os
import numpy as np
def correlation(x, y):
  mean_x = np.mean(x)
  mean_y = np.mean(y)

  X = x - mean_x
  Y = y - mean_y

  ans = (np.einsum('i,i -> ', X, Y) /
         np.sqrt(np.einsum('i,i -> ', X, X) * np.einsum('j,j -> ', Y, Y)))
  return ans

def main():
  file_url = 'https://drive.google.com/uc?id=1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'
  output = ('./data/advertising.csv')

  if not os.path.exists(output):
    print(f"File chưa tồn tại. Đang tải về {output}...")
    gdown.download(file_url, output, quiet=False)
    print(f"File đã được tải về với tên: {output}")

  data = pd.read_csv("./data/advertising.csv")

  x = data['TV']
  y = data['Radio']
  corr_xy = correlation(x, y)
  print(f"Correlation between TV and Sales : {round(corr_xy, 2)}")


if __name__ == "__main__":
  main()
