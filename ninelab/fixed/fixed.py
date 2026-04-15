import struct
numbers = []
sum = 0
with open("numbers.dat", "rb") as f:
    while True:
        a = f.read(4)
        if not a:
            break
        num = struct.unpack("i", a)[0]
        numbers.append(num)
        sum = sum + num

print("Десятичні числа:", numbers)
print("Cума:", sum)
