s = 0      
count = 0  

while True:
    num = int(input("Введи число (0 для виходу): "))
    if num == 0:
        break
    s += num
    count += 1

if count > 0:
    print("Середнє значення:", s / count)
else:
    print("Порожньо")
