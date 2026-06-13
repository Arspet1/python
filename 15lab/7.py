#Реалізуйте функцію, яка приймає список чисел і повертає новий список з квадратами цих чисел,
#  використовуючи map().
def squares(numbers):
    return list(map(lambda x: x ** 2, numbers))


print(squares([1, 2, 3, 4]))