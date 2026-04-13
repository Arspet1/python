# task6.py
count = 0
with open("mbox-short.txt","r",encoding="utf-8") as f:
    for line in f:
        if "@" in line:
            print(line.strip())
            count += 1

print("Кількість рядків з @: ", count)
