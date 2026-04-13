# task4.py
with open("mbox-short.txt","r",encoding="utf-8") as f:
    lines = f.readlines()

for l in lines:
    print(len(l.strip()))

words = " ".join(lines).split()
longest = max(words, key=len)
print("Найдовше слово:", longest)
