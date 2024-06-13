# import gdown
# url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
# output = 'P1_data.txt'
# gdown.download(url, output, quiet=False)

def count_chars_many_lines(content):
    my_dict = {}
    print(content)
    for line in content:
        vocabs = line.split()
        for vocab in vocabs:
            vocab = vocab.lower()
            if vocab in my_dict:
                my_dict[vocab] += 1
            else:
                my_dict[vocab] = 1
    return my_dict


file_path = 'module1\week2\P1_data.txt'
content = ''
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read().splitlines()
    

print(count_chars_many_lines(content))

