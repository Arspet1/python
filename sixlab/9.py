result = None
operand = None
operator = None
wait_for_number = True

while True: # <- без єтого кента все таки никак
    ravno = input()

    # если ждём число
   
    if ravno == "=": # таким образом при написании равно в терминале, мы получим результат, это лучше сделать с самого начала,чтобы цикл не пошел дальше и не сделал лишние подсчёты
            print("Result:", result)
            break
    if wait_for_number:        
        try:
            number = float(ravno)
        except:
            print(f"{ravno} Це не  число, добрий вечір...") # ловим на ошибке
            continue # <- узнал об єтой полезной штуке, шоб не гробить свой терминал, скипаем код после, если произойдёт ошибка
        if result is None: # просто сохраняем первое число
            result = number
        else:
            operand = number
             # вот уже калькулятор типо, но нема приоритета по знакам, но и бог с ним                    
            if operator == "+":
                result = result + operand
            elif operator == "-":
                result = result - operand
            elif operator == "*":
                result = result * operand
            elif operator == "/":
                result = result / operand

        wait_for_number = False

    # распознавание знаков чтобы соблюдался порядок написания примера
    else:
        if ravno not in ["+", "-", "*", "/"]: 
            print(f"{ravno} is not '+' or '-' or '/' or '*'. Try again")
            continue

        operator = ravno
        wait_for_number = True