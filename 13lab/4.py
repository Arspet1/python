from datetime import date, timedelta

def tomorrow(day, month, year):
    d = date(year, month, day)
    return d + timedelta(days=1)

def yesterday(day, month, year):
    d = date(year, month, day)
    return d - timedelta(days=1)

day = int(input("День: "))
month = int(input("Місяць: "))
year = int(input("Рік: "))

print("Вчора:", yesterday(day, month, year))
print("Завтра:", tomorrow(day, month, year))