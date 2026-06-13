import pandas as pd

population_dict = {
    'Kyiv': 2967360,
    'Kharkiv': 1443207,
    'Odesa': 1010537,
    'Dnipro': 968502,
    'Donetsk': 901645,
    'Zaporizhzhia': 710052,
    'Lviv': 717803,
    'Kryvyi Rih': 603904,
    'Mykolaiv': 470011,
    'Mariupol': 431859
}

# Створення Series
population = pd.Series(population_dict)

print("Series:")
print(population)

# Найбільше значення
print("\nМаксимальне населення:")
print(population.max())

# Найменше значення
print("\nМінімальне населення:")
print(population.min())

# Середнє значення
print("\nСереднє населення:")
print(population.mean())

# Населення Києва
print("\nНаселення Києва:")
print(population['Kyiv'])

# Перші 5 міст
print("\nПерші 5 міст:")
print(population.head())

# Додати Полтаву
population['Poltava'] = 279593

print("\nПісля додавання Полтави:")
print(population)

# Міста з населенням більше 1 млн
print("\nМіста з населенням > 1 000 000:")
print(population[population > 1000000])

# Всі міста
print("\nСписок міст:")
print(population.index)