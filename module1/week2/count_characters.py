
def count_chars(string):
    my_dict = {}
    for char in string:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


string = 'Happiness'
print(count_chars(string))
string = 'smiles'
print(count_chars(string))

