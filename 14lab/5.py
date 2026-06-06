from functools import reduce

a = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]

result = reduce(lambda x, y: x * y, a)

print(result)