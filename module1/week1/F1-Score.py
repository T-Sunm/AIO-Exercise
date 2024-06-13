def exercise1(tp, fp, fn):
  for var, name in zip([tp, fp, fn], ["tp", "fp", "fn"]):
    if (type(var) is not int):
      print(f'{name} must be int')
      return
    elif (var <= 0):
      print(f"{name} must be greater than zero")
      return
  precision = tp / (tp + fp)
  recall = tp / (tp + fn)
  f1_score = 2 * ((precision * recall) / (precision + recall))

  print(f"precision is {precision}")
  print(f"recall is {recall}")
  print(f"f1 - score is {f1_score}")


exercise1(tp=2, fp=3, fn=4)
exercise1(tp='a', fp=3, fn=4)
exercise1(tp=2, fp='a', fn=4)
exercise1(tp=2, fp=3, fn='a')
exercise1(tp=2, fp=3, fn=0)
exercise1(tp=2.1, fp=3, fn=0)
