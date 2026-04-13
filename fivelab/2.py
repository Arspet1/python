number = int(input("Введи чотиризначне число: "))
s = 0

while number > 0:
    digit = number % 10
    s = s + digit
    number = number // 10

print("Сума цифр:", s)
