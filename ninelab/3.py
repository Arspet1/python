a = [10,20,30,20,10,50,60,40,80,50,40]
print(a)
a = sorted(a)
for i in range(len(a)-1, 0, -1):
    if a[i] == a[i-1]:
        a.remove(a[i])

print(a)        
