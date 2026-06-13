#Створіть функцію is_palindrome(word), яка перевіряє, чи є слово паліндромом.
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


print(is_palindrome("Alla"))
print(is_palindrome("Alya"))