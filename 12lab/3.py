import numpy as np

arr = np.array([10, 20, 30, 40, 50])

num = int(input("Введіть число для перевірки: "))

if num in arr:
    print("Число є в масиві")
else:
    print("Числа немає в масиві")