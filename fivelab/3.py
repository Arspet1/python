s = 0  
while True:
    num = int(input("Введи число (мінус для виходу): "))
    if num < 0:
        break  
    s += num

print("Сума додатних чисел:", s)
