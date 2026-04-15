import re

with open("mbox-short.txt", "r") as f:
    text = f.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
count = len(emails)

for i in emails:
    print(i)
print("There were " + str(count) + " lines in the file with From as the first word")