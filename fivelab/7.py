import random
random_number = random.randint(1,10)
while True:
    answer = int(input())
    if answer == random_number:
        print('Ви вгадали')
    elif answer  < random_number:
        print('Більше')
    elif answer > random_number:
        print('Менше')
    if answer == exit:
        print('Ви вийшли')
        break
