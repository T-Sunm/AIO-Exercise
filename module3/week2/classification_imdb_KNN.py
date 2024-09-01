import numpy as np
from datasets import load_dataset
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

def main():
  imdb = load_dataset("imdb")
  imdb_train, imdb_test = imdb['train'], imdb['test']

  vectorizer = CountVectorizer(max_features=1000)
  x_train = vectorizer.fit_transform(imdb_train['text']).toarray()
  x_test = vectorizer.transform(imdb_test['text']).toarray()
  y_train = imdb_train['label']
  y_test = imdb_test['label']

  # Scale the features using StandardScaler
  scaler = StandardScaler()
  x_train = scaler.fit_transform(x_train)
  x_test = scaler.transform(x_test)

  knn_classifier = KNeighborsClassifier(n_neighbors=1, algorithm='ball_tree')
  knn_classifier.fit(x_train, y_train)

  y_pred = knn_classifier.predict(x_test)
  print(accuracy_score(y_true=y_test, y_pred=y_pred))


if __name__ == '__main__':
  main()
