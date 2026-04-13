arr = []
for i in range(10):
    a = int(input())
    arr.append(a)


for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print('парне ', arr[i])