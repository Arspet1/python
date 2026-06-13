#Напишіть функцію, яка приймає список чисел і повертає кортеж (мінімум, максимум, середнє значення).
def analyze_numbers(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return (minimum, maximum, average)


print(analyze_numbers([1, 2, 3, 4, 5]))