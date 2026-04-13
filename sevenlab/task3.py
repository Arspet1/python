# task3.py
with open("poetry.txt","r",encoding="utf-8") as f:
    lines = f.readlines()

not_T = sum(1 for l in lines if not l.startswith("T"))
end_d = sum(1 for l in lines if l.strip().endswith("d"))

words = " ".join(lines).split()
capital_words = sum(1 for w in words if w[0].isupper())

print("Рядків не з T:", not_T)
print("Рядків що закінчуються на d:", end_d)
print("Слів з великої літери:", capital_words)
