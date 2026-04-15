# Написати програму, яка знаходить суму усіх елементів списку.
import random
arr = []
for i in range(10):
    a = random.randint(1, 100)
    arr.append(a)

sum = 0
for i in arr:
    sum = sum + i
print("List:", arr, "\nSum:", sum)    