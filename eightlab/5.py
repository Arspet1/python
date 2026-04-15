with open("report.txt", "r") as f:
    content = f.read()
content = content.replace("old", "new")

with open("report.txt", "w") as f:
    f.write(content)

print(content)            