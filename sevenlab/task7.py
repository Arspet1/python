# task7.py
pos = []
neg = []

with open("feedback.txt","r",encoding="utf-8") as f:
    lines = f.readlines()

for l in lines:
    if l.startswith("Positive"):
        pos.append(l)
    elif l.startswith("Negative"):
        neg.append(l)

with open("positive.txt","w",encoding="utf-8") as f:
    f.writelines(pos)

with open("negative.txt","w",encoding="utf-8") as f:
    f.writelines(neg)

with open("feedback_analysis.txt","w",encoding="utf-8") as f:
    f.write(f"Total feedbacks: {len(lines)}\n")
    f.write(f"Count of positive feedbacks: {len(pos)}\n")
    f.write(f"Count of negative feedbacks: {len(neg)}\n")

print("Аналіз завершено.")
