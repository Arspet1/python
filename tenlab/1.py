with open("dict.txt", "r", encoding="utf-8") as f:
    dict_lines = f.readlines()

dictionary = {}

for line in dict_lines:
    line = line.strip() 
    parts = line.split("\t-\t")  
    if len(parts) == 2:
        key = parts[0]
        value = parts[1]
        dictionary[key] = value

with open("translate.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()

translated_words = []

for word in words:
    if word in dictionary:
        translated_words.append(dictionary[word])
    else:
        translated_words.append(word)

result = " ".join(translated_words)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result)