word = input("Введіть будь-який текст: ")

letters = "aeiyouAEIYOU" 
i = 0

while i < len(word):
    if word[i] not in letters:
        print(word[i], end="")

    i = i + 1
