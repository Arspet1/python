arr = []
for i in range(10):
    a = int(input())
    arr.append(a)

dob = 1
print(arr)
for j in range(len(arr) - 1):
    dob *= arr[j]

print(dob)