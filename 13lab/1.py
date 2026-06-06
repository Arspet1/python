def bank(x, years):
    for i in range(years):
        x = x * 1.10
    return x

money = float(input("Внесок: "))
years = int(input("Кількість років: "))

print("На рахунку буде:", bank(money, years))