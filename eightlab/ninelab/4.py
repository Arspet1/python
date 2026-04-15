words = []
with open("romeo.txt", "r") as f:
    for i in f:
        line = i.split()
        for j in line:
            if j not in words:
                words.append(j)

words = sorted(words)
print(words)





      