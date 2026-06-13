#Напишіть функцію count_words(text), яка повертає словник, де ключ — слово, а значення — кількість
# його входжень у тексті.
def count_words(text):
    words = text.split()
    result = {}

    for word in words:
        result[word] = result.get(word, 0) + 1

    return result


print(count_words("кіт пес кіт"))