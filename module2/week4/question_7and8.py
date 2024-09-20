import pandas as pd
import gdown
import os
import numpy as np


def main():
  file_url = 'https://drive.google.com/uc?id=1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'
  output = ("./data/advertising.csv")

  if not os.path.exists(output):
    print(f"File chưa tồn tại. Đang tải về {output}...")
    gdown.download(file_url, output, quiet=False)
    print(f"File đã được tải về với tên: {output}")

  data = pd.read_csv("./data/advertising.csv")

  # ------ Excercise 7----------
  x = data['Radio']
  y = data['Newspaper']
  result = np.corrcoef(x, y)
  print("Excercise 7: \n", result)

  print()

  # ------ Excercise 8----------
  print("Excercise 8: \n", data.corr())


if __name__ == "__main__":
  main()
