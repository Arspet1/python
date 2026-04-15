import random
import struct
with open("numbers.dat", "wb") as f:
    for i in range(10):
        num = random.randint(1, 100)
        f.write(struct.pack("i", num))

numbers = []
with open("numbers.dat", "rb") as f:
    for i in range(10):
        data = f.read(4)
        num = struct.unpack("i", data)[0]
        numbers.append(num)

print("Масив", numbers)
print("Сума:", sum(numbers))

