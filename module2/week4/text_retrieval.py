import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.stats import pearsonr
import gdown
import os


def cosine_search(question: str, context_embedded, tfidf_vectorizer: TfidfVectorizer, top_d=5):
  # chuyển về lower rồi embedding
  query_embedded = tfidf_vectorizer.transform([question.lower()])
  cosine_scores = cosine_similarity(query_embedded, context_embedded)[0]

  top_d_value = np.argsort(cosine_scores)[-1:(-top_d - 1):-1]

  ans = []
  for index in top_d_value:
    doc_score = {
        'id': index,
        'cosine_score': cosine_scores[index]
    }
    ans.append(doc_score)

  return ans

def corr_search(question: str, context_embedded, tfidf_vectorizer: TfidfVectorizer, top_d=5):
   # chuyển về lower rồi embedding
  query_embedded = tfidf_vectorizer.transform([question.lower()]).toarray()[0]

  context_embedded = context_embedded.toarray()

  corr_scores = [pearsonr(query_embedded, context)[0]
                 for context in context_embedded]

  top_d_value = np.argsort(corr_scores)[-1:(-top_d - 1):-1]

  ans = []
  for index in top_d_value:
    doc_score = {
        'id': index,
        'corr_score': corr_scores[index]
    }
    ans.append(doc_score)

  return ans


def main():
  file_url = 'https://drive.google.com/uc?id=1jh2p2DlaWsDo_vEWIcTrNh3mUuXd-cw6'
  output = ("./data/vi_text_retrieval.csv")

  if not os.path.exists(output):
    print(f"File chưa tồn tại. Đang tải về {output}...")
    gdown.download(file_url, output, quiet=False)
    print(f"File đã được tải về với tên: {output}")

  vi_data_df = pd.read_csv("./data/vi_text_retrieval.csv")
  context = vi_data_df['text']
  context = [doc.lower() for doc in context]


# -----------câu 10-----------------
  tfidf_vectorizer = TfidfVectorizer()
  context_embedded = tfidf_vectorizer.fit_transform(context)
  print("Câu 10 :", np.round(context_embedded.toarray()[7][0], 2))


# ----------- câu 11-------------------
# lấy câu hỏi đầu tiên
  question = vi_data_df.iloc[0]['question']
  results = cosine_search(question, context_embedded,
                          tfidf_vectorizer, top_d=5)
  print("Câu 11 :", np.round(results[0]['cosine_score'], 2))

# ----------- câu 12------------------
  results = corr_search(question, context_embedded, tfidf_vectorizer, top_d=5)
  print("câu 12 :", np.round(results[1]['corr_score'], 2))


if __name__ == "__main__":
  main()
