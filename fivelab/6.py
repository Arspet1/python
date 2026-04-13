number = 0 
while True:
    age = input("Введіть ваш вік (або 'exit' для виходу): ")
    
    if age == 'exit':
        break
    
    number = number + 1 
    age = int(age)
    
    if age < 3:
        print("Квиток безкоштовний")
    elif age <= 12:
        print("Вартість квитка — 50 грн")
    else:
        print("Вартість квитка — 80 грн")
    
    print("Це було запитання №", number)

print("Кінець. Всього запитів:", number)
