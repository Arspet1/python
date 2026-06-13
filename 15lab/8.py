#Реалізуйте функцію, яка створює таблицю множення до заданого числа n (наприклад, до 5 — це 5x5 таблиця),
#  і повертає її у вигляді вкладених списків.
def multiplication_table(n):
    table = []

    for i in range(1, n + 1):
        row = []

        for j in range(1, n + 1):
            row.append(i * j)

        table.append(row)

    return table


print(multiplication_table(5))