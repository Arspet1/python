import numpy as np

arr = np.random.randint(1, 10, (3, 3))

print("Матриця:")
print(arr)

det = np.linalg.det(arr)

print("Визначник:", det)