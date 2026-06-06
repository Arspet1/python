words = input("Введіть слова через дефіс: ")

words_list = words.split("-")
words_list.sort()

print("-".join(words_list))