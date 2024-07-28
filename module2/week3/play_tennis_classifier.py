
import numpy as np
import pandas as pd
def create_train_data():
  data = [
      ['Sunny', 'Hot', 'High', 'Weak', 'no'],
      ['Sunny', 'Hot', 'High', 'Strong', 'no'],
      ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
      ['Rain', 'Mild', 'High', 'Weak', 'yes'],
      ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
      ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
      ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
      ['Overcast', 'Mild', 'High', 'Weak', 'no'],
      ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
      ['Rain', 'Mild', 'Normal', 'Weak', 'yes']
  ]

  columns = ['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis']

  return pd.DataFrame(data=data, columns=columns)

def compute_prior_probablity(train_data: pd.DataFrame):
  y_train = train_data.iloc[:, -1].values
  y_unique = list(set(y_train))
  prior_count = np.zeros(len(y_unique))
  prior_probablity = {}
  for data in y_train:
    index = y_unique.index(data)
    prior_count[index] += 1

  for label, count in zip(y_unique, prior_count):
    prior_probablity[label] = count / y_train.shape[0]

  return prior_probablity

def compute_conditional_probability(train_data: pd.DataFrame):
  y_train = train_data.iloc[:, -1].values
  y_unique = list(set(y_train))

  list_x_name = {}
  conditional_probability = {}
  for col in train_data.columns:
    x_unique = np.unique(train_data[col])
    list_x_name[col] = x_unique

  for y in y_unique:
    y_data = train_data[train_data['PlayTennis'] == y]
    y_prob = {}

    for col in y_data.columns[: -1]:
      value_in_feature_unique = np.unique(y_data[col])
      x_prob = np.zeros(len(value_in_feature_unique))

      for index, name in enumerate(value_in_feature_unique):
        # hàm tính số lần xuất hiện của giá trị trong từng cột
        x_count = y_data[col].value_counts().get(name, 0)
        x_prob[index] = x_count / y_data.shape[0]
      y_prob[col] = x_prob

    conditional_probability[y] = y_prob
  return conditional_probability, list_x_name

# This function is used to return the index of the feature name
def get_index_from_value(feature_name: str, list_features: np):
  return np.nonzero(list_features == feature_name)[0][0]

# ##########################
# Train Naive Bayes Model
# ##########################
def train_naive_bayes(train_data):
  # Step 1: Calculate Prior Probability
  prior_probability = compute_prior_probablity(train_data)

  # Step 2: Calculate Conditional Probability
  conditional_probability, list_x_name = compute_conditional_probability(
      train_data)

  return prior_probability, conditional_probability, list_x_name

# ###################
# Prediction
# ###################
def prediction_play_tennis(x, list_x_name, prior_probability, conditional_probability):
  x1 = get_index_from_value(x[0], list_x_name['Outlook'])
  x2 = get_index_from_value(x[1], list_x_name['Temperature'])
  x3 = get_index_from_value(x[2], list_x_name['Humidity'])
  x4 = get_index_from_value(x[3], list_x_name['Wind'])

  p0 = 0
  p1 = 0
  p_outlook_play_yes = round(conditional_probability['yes']['Outlook'][x1], 2)
  p_temperature_play_yes = round(
      conditional_probability['yes']['Temperature'][x2], 2)
  p_humidity_play_yes = round(
      conditional_probability['yes']['Humidity'][x3], 2)
  p_wind_play_yes = round(conditional_probability['yes']['Wind'][x4], 2)

  p_outlook_play_no = round(conditional_probability['no']['Outlook'][x1], 2)
  p_temperature_play_no = round(
      conditional_probability['no']['Temperature'][x2], 2)
  p_humidity_play_no = round(
      conditional_probability['no']['Humidity'][x3], 2)
  p_wind_play_no = round(conditional_probability['no']['Wind'][x4], 2)

  p_x_play_yes = p_outlook_play_yes * p_temperature_play_yes * \
      p_humidity_play_yes * p_wind_play_yes * prior_probability["yes"]
  p_x_play_no = p_outlook_play_no * p_temperature_play_no * \
      p_humidity_play_no * p_wind_play_no * prior_probability["no"]

  total = p_x_play_yes + p_x_play_no

  p0 = p_x_play_no / total
  p1 = p_x_play_yes / total

  if p0 > p1:
    y_pred = 0
  else:
    y_pred = 1

  print(p0, p1)
  return y_pred

def main():
  print("-------Ex 4.1----------")
  train_data = create_train_data()
  print(train_data, "\n")

  print("-------Ex 4.2----------")
  prior_probablity = compute_prior_probablity(train_data)
  print("P(play tennis = No ) = ", prior_probablity["no"])
  print("P(play tennis = Yes ) = ", prior_probablity["yes"], "\n")

  print("-------Ex 4.3----------")
  _, list_x_name = compute_conditional_probability(train_data)
  print("x1 = ", list_x_name['Outlook'])
  print("x2 = ", list_x_name['Temperature'])
  print("x3 = ", list_x_name['Humidity'])
  print("x4 = ", list_x_name['Wind'], "\n")

  print("-------Ex 4.4----------")
  outlook = list_x_name['Outlook']
  i1 = get_index_from_value("Overcast", outlook)
  i2 = get_index_from_value("Rain", outlook)
  i3 = get_index_from_value("Sunny", outlook)

  print(i1, i2, i3, '\n')

  conditional_probability, list_x_name = compute_conditional_probability(
      train_data)
  outlook = list_x_name['Outlook']
  i = get_index_from_value("Sunny", outlook)
  # print(conditional_probability)
  print("P('Outlook'= 'Sunny'|'Play Tennis'= 'Yes') = ",
        np.round(conditional_probability['yes']['Outlook'][i], 2))
  print("P('Outlook'= 'Sunny'|'Play Tennis'= 'No') = ",
        np.round(conditional_probability['no']['Outlook'][i], 2), '\n')

  print("-------Ex 4.5,4.6----------")
  X = ['Sunny', 'Cool', 'High', 'Strong']
  data = create_train_data()
  prior_probability, conditional_probability, list_x_name = train_naive_bayes(
      data)
  pred = prediction_play_tennis(
      X, list_x_name, prior_probability, conditional_probability)

  if (pred):
    print("Ad should go!")
  else:
    print("Ad should not go!")


if __name__ == "__main__":
  main()
