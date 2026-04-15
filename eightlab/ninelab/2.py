arr = []
print("Накидайте 5 чисел")
for i in range(5):
    a = int(input())
    arr.append(a)

print(arr)
for j in range(5):
    if arr[j] > 9 or arr[j] < -9:
        print(arr[j])    