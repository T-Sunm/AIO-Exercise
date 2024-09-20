import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():
  data = pd.read_csv("./data/advertising.csv")
  data_corr = data.corr()
  plt.figure(figsize=(10, 8))
#   annot = True giúp hiện số trên mỗi ô
  sns.heatmap(data=data_corr, annot=True, fmt=".2f", linewidths=.5)
  plt.show()


if __name__ == "__main__":
  main()
