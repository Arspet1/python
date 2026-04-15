count = 0

with open("log.txt", "r") as f, open("errors.txt", "w") as j:
    for i in f:
        if "ERROR" in i:
            j.write(i)
            count += 1

print('кількість: ', count)
