
def character_count(string):
  my_dict = {}
  for char in string:
    if char in my_dict:
      my_dict[char] += 1
    else:
      my_dict[char] = 1
  return my_dict


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
