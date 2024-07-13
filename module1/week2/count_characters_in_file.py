import gdown
url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
output = 'P1_data.txt'
gdown.download(url, output, quiet=False)

def count_chars_many_lines(content):
  my_dict = {}
  for line in content:
    vocabs = line.split()
    for vocab in vocabs:
      vocab = vocab.lower()
      my_dict[vocab] = my_dict.get(vocab, 0) + 1
  return my_dict


file_path = 'module1\week2\P1_data.txt'
content = ''
with open(file_path, 'r', encoding='utf-8') as file:
  content = file.read().splitlines()


result = count_chars_many_lines(content=content)
assert result['who'] == 3
print(result['man'])
